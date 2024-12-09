"""Generation prompt templates."""

from string import Template

class GenerationPrompts:
    """Templates for question generation prompts."""
    
    MCQ = Template("""
    You are a psychometrician turned high school teacher creating AP-level multiple choice questions.
    
    Article: ${article}
    Essential Knowledge Codes: ${ek_codes}
    Learning Objectives: ${lo_codes}
    
    Write exactly six multiple choice questions that:
    - Test understanding and application of the article content
    - Use appropriate Bloom's taxonomy task verbs
    - Connect to the provided learning objectives
    - Follow these criteria: ${criteria}
    
    Each question must:
    - Have exactly one correct answer
    - Have 3-4 plausible but incorrect distractors
    - Be answerable in one sentence
    - Not exceed difficulty level ${difficulty}
    
    Format your response as JSON with this structure:
    {
        "questions": [
            {
                "text": "question text",
                "correct_answer": "correct answer text",
                "distractors": ["distractor1", "distractor2", "distractor3"],
                "explanation": "why this is correct",
                "ek_code": "relevant code",
                "lo_code": "relevant code"
            }
        ]
    }
    """)

    CORRECT_ANSWER = Template("""
    You are an AP exam expert creating the correct answer for this question:
    
    Question: ${question}
    
    Requirements:
    - Answer must be factually correct based on ${article}
    - Use one sentence of maximum 20 words
    - Follow the task verb correctly
    - Address all parts of the question
    - Follow these criteria: ${criteria}
    
    Format your response as JSON with this structure:
    {
        "answer": "your answer",
        "justification": "why this is correct"
    }
    """)

    DISTRACTORS = Template("""
    You are an AP exam expert creating plausible but incorrect answers for this question:
    
    Question: ${question}
    Correct Answer: ${correct_answer}
    
    Create exactly ${num_distractors} distractors that:
    - Are clearly incorrect but believable
    - Follow the same structure as the correct answer
    - Are similar in length and complexity
    - Avoid absolute terms
    - Follow these criteria: ${criteria}
    
    Format your response as JSON with this structure:
    {
        "distractors": [
            {
                "text": "distractor text",
                "explanation": "why this is incorrect"
            }
        ]
    }
    """)
