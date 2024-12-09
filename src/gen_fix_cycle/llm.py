"""LLM interaction module using Anthropic's Claude."""

import json
import os
from dataclasses import asdict
from typing import Any, Dict, Optional

import anthropic
from .config import LLMConfig
from .models import Question, Response, QuestionType, Difficulty, QCResult

class LLMClient:
    """Client for LLM interactions using Claude."""
    
    def __init__(self, config: LLMConfig):
        self.config = config
        self.client = anthropic.Client(api_key=os.getenv("ANTHROPIC_API_KEY"))
        
    def complete(self, prompt: str) -> Dict[str, Any]:
        """Send prompt to Claude and parse JSON response."""
        response = self.client.messages.create(
            model=self.config.model,
            max_tokens=self.config.max_tokens,
            temperature=self.config.temperature,
            system="You are an expert in AP assessment design. Always respond in valid JSON format.",
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract and parse JSON from response
        try:
            return json.loads(response.content[0].text)
        except (json.JSONDecodeError, KeyError, IndexError) as e:
            raise ValueError(f"Failed to parse LLM response as JSON: {e}")

    def generate_question(
        self,
        article: str,
        ek_codes: Optional[str],
        lo_codes: Optional[str],
        criteria: str,
        difficulty: str,
        existing_questions: Optional[str] = None
    ) -> Dict[str, Any]:
        """Generate a new question."""
        prompt = f"""
        You are a psychometrician turned high school teacher. Your task is building AP level learning assessments.
        
        The assessment is to test whether students read this article: {article}
        
        Requirements:
        - Use task verbs from Bloom's taxonomy
        - Connect article information to student understanding
        - Follow these criteria: {criteria}
        - Specify which ek_code and lo_code it addresses from: {ek_codes or 'N/A'} and {lo_codes or 'N/A'}
        - Target difficulty level: {difficulty}
        - Do not refer to the article in the question
        {"- Ensure question is not similar to: " + existing_questions if existing_questions else ""}
        
        Output your response in this exact JSON format:
        {{
            "text": "question text",
            "correct_answer": "correct answer text",
            "distractors": ["distractor1", "distractor2", "distractor3"],
            "explanation": "why this is correct",
            "ek_code": "relevant code",
            "lo_code": "relevant code"
        }}
        """
        return self.complete(prompt)

    def quality_check(
        self,
        question: str,
        responses: str,
        check_type: str,
        criteria: str
    ) -> Dict[str, Any]:
        """Run a quality check on a question."""
        prompt = f"""
        As a world-renowned expert in educational assessment with 30 years of experience designing AP exams,
        evaluate this question's {check_type}.
        
        Question to evaluate: {question}
        Responses: {responses}
        
        Criteria: {criteria}
        
        Score 1 if ALL criteria are met, 0 if ANY are not met.
        Provide a 2-line explanation and 2 lines of actionable feedback.
        
        Output your response in this exact JSON format:
        {{
            "score": 0 or 1,
            "rationale": "Your 2-line explanation here",
            "feedback": "Your 2-line feedback here"
        }}
        """
        return self.complete(prompt)

    def fix_question(
        self,
        question: str,
        responses: str,
        feedback: str,
        fix_type: str
    ) -> Dict[str, Any]:
        """Fix issues in a question based on QC feedback."""
        prompt = f"""
        As a world-renowned expert in educational assessment,
        improve this question's {fix_type} based on QC feedback.
        
        Question: {question}
        Responses: {responses}
        Feedback: {feedback}
        
        Output your response in this exact JSON format:
        {{
            "revision_status": "revision necessary/no revision necessary",
            "revised_question": "Your improved version of the question",
            "revised_responses": {{
                "correct": "revised correct answer",
                "distractors": [
                    "revised distractor 1",
                    "revised distractor 2",
                    "revised distractor 3"
                ]
            }},
            "explanation": "what was changed and why"
        }}
        """
        return self.complete(prompt)
