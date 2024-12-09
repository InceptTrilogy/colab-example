"""Quality check implementation."""

from dataclasses import asdict
from typing import Dict, List

from ..llm import LLMClient, parse_qc_response
from ..models import Question, QCResult
from .qc_prompts import QualityCheckPrompts

def format_responses(question: Question) -> str:
    """Format responses for prompts."""
    return "\n".join(
        f"{i+1}. {r.text}" + (f" (Explanation: {r.explanation})" if r.explanation else "")
        for i, r in enumerate(question.responses)
    )

class QualityChecker:
    """Manages the quality check process for questions."""
    
    def __init__(self, llm: LLMClient):
        self.llm = llm
        self.prompts = QualityCheckPrompts()
        self.checks = ['clarity', 'format', 'content', 'difficulty']
    
    def check_clarity(self, question: Question) -> QCResult:
        """Run clarity check."""
        prompt = self.prompts.CLARITY.substitute(
            question=question.text,
            responses=format_responses(question)
        )
        response = self.llm.complete(prompt)
        return parse_qc_response(response)
    
    def check_format(self, question: Question) -> QCResult:
        """Run format check."""
        prompt = self.prompts.FORMAT.substitute(
            question=question.text,
            responses=format_responses(question)
        )
        response = self.llm.complete(prompt)
        return parse_qc_response(response)
    
    def check_content(
        self,
        question: Question,
        article: str
    ) -> QCResult:
        """Run content check."""
        prompt = self.prompts.CONTENT.substitute(
            question=question.text,
            responses=format_responses(question),
            article=article,
            ek_code=question.ek_code or "N/A",
            lo_code=question.lo_code or "N/A"
        )
        response = self.llm.complete(prompt)
        return parse_qc_response(response)
    
    def check_difficulty(self, question: Question) -> QCResult:
        """Run difficulty check."""
        prompt = self.prompts.DIFFICULTY.substitute(
            question=question.text,
            responses=format_responses(question)
        )
        response = self.llm.complete(prompt)
        return parse_qc_response(response)
    
    def run_all_checks(
        self,
        question: Question,
        article: str
    ) -> List[QCResult]:
        """Run all quality checks on a question."""
        return [
            self.check_clarity(question),
            self.check_format(question),
            self.check_content(question, article),
            self.check_difficulty(question)
        ]
