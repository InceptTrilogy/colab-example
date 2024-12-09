"""Quality check prompt templates."""

from string import Template

class QualityCheckPrompts:
    """Templates for quality check prompts."""
    
    CLARITY = Template("""
    As an AP assessment expert, evaluate this question's clarity:
    
    Question: ${question}
    Responses: ${responses}
    
    Score 1 if ALL conditions are met:
    - Has single, clear interpretation
    - Provides sufficient context
    - Uses precise language
    - Avoids compound questions
    
    Score 0 if ANY condition is not met.
    
    Format response as JSON:
    {
        "score": 0 or 1,
        "rationale": "2-line explanation",
        "feedback": "2-line actionable feedback"
    }
    """)
    
    FORMAT = Template("""
    As an AP assessment expert, evaluate this question's format:
    
    Question: ${question}
    Responses: ${responses}
    
    Score 1 if ALL conditions are met:
    - Has 4-5 answer options
    - All formulas properly formatted
    - All referenced materials present
    - Consistent formatting across options
    
    Score 0 if ANY condition is not met.
    
    Format response as JSON:
    {
        "score": 0 or 1,
        "rationale": "2-line explanation",
        "feedback": "2-line actionable feedback"
    }
    """)
    
    CONTENT = Template("""
    As an AP assessment expert, evaluate this question's content:
    
    Question: ${question}
    Responses: ${responses}
    Article: ${article}
    EK Code: ${ek_code}
    LO Code: ${lo_code}
    
    Score 1 if ALL conditions are met:
    - Answerable through critical thinking and article content
    - Uses correct terminology
    - Aligns with EK/LO codes
    - Culturally sensitive and appropriate
    - Not redundant with other questions
    
    Score 0 if ANY condition is not met.
    
    Format response as JSON:
    {
        "score": 0 or 1,
        "rationale": "2-line explanation",
        "feedback": "2-line actionable feedback"
    }
    """)
    
    DIFFICULTY = Template("""
    As an AP assessment expert, evaluate this question's difficulty:
    
    Question: ${question}
    Responses: ${responses}
    
    Assign difficulty level:
    0: Reading comprehension (explicit in text)
    1: Recall (Bloom's Easy)
    2: Analysis (Bloom's Moderate)
    3: Evaluation (Bloom's Difficult)
    
    Score 1 if difficulty > 0, 0 if difficulty = 0
    
    Format response as JSON:
    {
        "score": 0 or 1,
        "difficulty": "0-3",
        "rationale": "2-line explanation",
        "feedback": "2-line actionable feedback"
    }
    """)
