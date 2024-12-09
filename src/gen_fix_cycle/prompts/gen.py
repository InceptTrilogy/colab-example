"""Question generation implementation."""

from typing import List, Optional

from ..llm import LLMClient
from ..models import Question, Response, QuestionType, Difficulty
from .gen_prompts import GenerationPrompts

class QuestionGenerator:
    """Manages the question generation process."""
    
    def __init__(self, llm: LLMClient):
        self.llm = llm
        self.prompts = GenerationPrompts()
    
    def generate_mcq(
        self,
        article: str,
        ek_codes: Optional[List[str]],
        lo_codes: Optional[List[str]],
        criteria: str,
        difficulty: Difficulty
    ) -> List[Question]:
        """Generate multiple choice questions."""
        prompt = self.prompts.MCQ.substitute(
            article=article,
            ek_codes=", ".join(ek_codes) if ek_codes else "N/A",
            lo_codes=", ".join(lo_codes) if lo_codes else "N/A",
            criteria=criteria,
            difficulty=difficulty.value
        )
        
        response = self.llm.complete(prompt)
        questions = []
        
        for q in response.get("questions", []):
            responses = [
                Response(
                    text=q["correct_answer"],
                    is_correct=True,
                    explanation=q.get("explanation")
                )
            ] + [
                Response(text=d, is_correct=False)
                for d in q.get("distractors", [])
            ]
            
            questions.append(Question(
                text=q["text"],
                responses=responses,
                question_type=QuestionType.MCQ,
                difficulty=difficulty,
                ek_code=q.get("ek_code"),
                lo_code=q.get("lo_code")
            ))
            
        return questions
    
    def generate_correct_answer(
        self,
        question: str,
        article: str,
        criteria: str
    ) -> Optional[Response]:
        """Generate a correct answer for a question."""
        prompt = self.prompts.CORRECT_ANSWER.substitute(
            question=question,
            article=article,
            criteria=criteria
        )
        
        response = self.llm.complete(prompt)
        if not response.get("answer"):
            return None
            
        return Response(
            text=response["answer"],
            is_correct=True,
            explanation=response.get("justification")
        )
    
    def generate_distractors(
        self,
        question: str,
        correct_answer: str,
        num_distractors: int,
        criteria: str
    ) -> List[Response]:
        """Generate distractor options."""
        prompt = self.prompts.DISTRACTORS.substitute(
            question=question,
            correct_answer=correct_answer,
            num_distractors=num_distractors,
            criteria=criteria
        )
        
        response = self.llm.complete(prompt)
        return [
            Response(
                text=d["text"],
                is_correct=False,
                explanation=d.get("explanation")
            )
            for d in response.get("distractors", [])
        ]

def get_generation_prompt(
    prompt_type: str,
    **kwargs
) -> str:
    """Get a formatted generation prompt."""
    templates = {
        'mcq': GenerationPrompts.MCQ,
        'correct': GenerationPrompts.CORRECT_ANSWER,
        'distractors': GenerationPrompts.DISTRACTORS
    }
    
    template = templates.get(prompt_type)
    if not template:
        raise ValueError(f"Unknown prompt type: {prompt_type}")
        
    return template.substitute(**kwargs)
