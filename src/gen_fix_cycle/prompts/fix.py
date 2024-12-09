"""Question fixing implementation."""

from dataclasses import asdict
from typing import Dict, List, Optional

from ..llm import LLMClient
from ..models import Question, QCResult, Response
from .fix_prompts import FixPrompts
from .qc import format_responses

class QuestionFixer:
    """Manages the question fixing process."""
    
    def __init__(self, llm: LLMClient):
        self.llm = llm
        self.prompts = FixPrompts()
        self.fix_types = ['clarity', 'responses', 'difficulty']
    
    def fix_clarity(
        self,
        question: Question,
        feedback: str
    ) -> Optional[Question]:
        """Fix clarity issues."""
        prompt = self.prompts.CLARITY.substitute(
            question=question.text,
            feedback=feedback
        )
        response = self.llm.complete(prompt)
        
        if not response.get('revised_question'):
            return None
            
        fixed = Question(
            text=response['revised_question'],
            responses=question.responses,
            question_type=question.question_type,
            difficulty=question.difficulty,
            ek_code=question.ek_code,
            lo_code=question.lo_code,
            skill_code=question.skill_code
        )
        return fixed
    
    def fix_responses(
        self,
        question: Question,
        feedback: str
    ) -> Optional[Question]:
        """Fix response issues."""
        prompt = self.prompts.RESPONSES.substitute(
            question=question.text,
            responses=format_responses(question),
            feedback=feedback
        )
        response = self.llm.complete(prompt)
        
        if not response.get('revised_responses'):
            return None
            
        revised = response['revised_responses']
        responses = [
            Response(text=revised['correct'], is_correct=True)
        ] + [
            Response(text=d, is_correct=False)
            for d in revised['distractors']
        ]
        
        fixed = Question(
            text=question.text,
            responses=responses,
            question_type=question.question_type,
            difficulty=question.difficulty,
            ek_code=question.ek_code,
            lo_code=question.lo_code,
            skill_code=question.skill_code
        )
        return fixed
    
    def fix_question(
        self,
        question: Question,
        qc_results: List[QCResult]
    ) -> Optional[Question]:
        """Apply all needed fixes to a question."""
        current = question
        
        for result in qc_results:
            if result.score == 0:
                if result.rationale == 'clarity':
                    fixed = self.fix_clarity(current, result.feedback)
                    if fixed:
                        current = fixed
                elif result.rationale in ['format', 'responses']:
                    fixed = self.fix_responses(current, result.feedback)
                    if fixed:
                        current = fixed
                        
        return current if current != question else None
