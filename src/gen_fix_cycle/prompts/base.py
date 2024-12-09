"""Base templates and generator class for prompts."""

from string import Template
from typing import Dict, Optional

class PromptTemplate:
    """Base templates for different prompt types."""
    
    GEN_QUESTION = Template("""
    You are a psychometrician turned high school teacher. Your task is building AP level learning assessments.

    The assessment is to test whether students read this article: ${article}

    Requirements:
    - Use task verbs from Bloom's taxonomy to write exactly six questions
    - Questions should prove students can connect article information to their understanding
    - Do not write duplicate questions
    - Follow these criteria: ${criteria}
    - Specify which ek_code and lo_code each question addresses
    - All questions should have difficulty: ${difficulty}
    - Do not refer to the article in the question

    Please output your response in JSON format.
    """)

    GEN_CORRECT = Template("""
    You are a student taking an AP assessment.
    The teacher wants to ensure you understand how to connect ${ek_codes} and article information to ${lo_codes}.

    Question: ${question}

    Requirements:
    - Identify and follow the task verb from Bloom's taxonomy
    - Follow these criteria: ${criteria}
    - Answer in one sentence of less than 20 words
    - Use only information from the article
    - Response must be factually correct

    Please output your response in JSON format.
    """)

    QC_CLARITY = Template("""
    As an expert in educational assessment, evaluate this question's clarity:

    Question: ${question}
    Responses: ${responses}
    Article: ${article}

    Score 1 if ALL conditions are met:
    - Single clear interpretation
    - Sufficient context provided
    - Referenced materials are included
    - Can be answered from article or critical thinking

    Score 0 if ANY condition is not met.

    Provide a 2-line explanation and 2 lines of actionable feedback.
    Please output your response in JSON format.
    """)

class PromptGenerator:
    """Generates prompts based on subject and context."""
    
    def __init__(self, subject: str):
        self.subject = subject
        self.templates = PromptTemplate()
        
    def get_gen_question_prompt(
        self,
        article: str,
        criteria: str,
        difficulty: str
    ) -> str:
        """Generate a question generation prompt."""
        return self.templates.GEN_QUESTION.substitute(
            article=article,
            criteria=criteria,
            difficulty=difficulty
        )
    
    def get_gen_correct_prompt(
        self,
        question: str,
        ek_codes: str,
        lo_codes: str,
        criteria: str
    ) -> str:
        """Generate a correct answer generation prompt."""
        return self.templates.GEN_CORRECT.substitute(
            question=question,
            ek_codes=ek_codes,
            lo_codes=lo_codes,
            criteria=criteria
        )
    
    def get_qc_clarity_prompt(
        self,
        question: str,
        responses: str,
        article: str
    ) -> str:
        """Generate a clarity QC prompt."""
        return self.templates.QC_CLARITY.substitute(
            question=question,
            responses=responses,
            article=article
        )
