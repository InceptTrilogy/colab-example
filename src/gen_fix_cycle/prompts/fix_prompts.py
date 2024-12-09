"""Fix prompt templates."""

from string import Template

class FixPrompts:
    """Templates for fix prompts."""
    
    CLARITY = Template("""
    As an AP assessment expert, improve this question's clarity:
    
    Original Question: ${question}
    QC Feedback: ${feedback}
    
    Requirements:
    - Ensure single, clear interpretation
    - Provide necessary context
    - Use precise language
    - Avoid compound questions
    - Maintain original intent
    
    Format response as JSON:
    {
        "revised_question": "improved question",
        "explanation": "what was changed and why"
    }
    """)
    
    RESPONSES = Template("""
    As an AP assessment expert, improve these response options:
    
    Question: ${question}
    Original Responses: ${responses}
    QC Feedback: ${feedback}
    
    Requirements:
    - Maintain similar length and structure
    - Use consistent terminology
    - Ensure one clearly correct answer
    - Make distractors plausible but clearly incorrect
    - Avoid absolute terms
    
    Format response as JSON:
    {
        "revised_responses": {
            "correct": "improved correct answer",
            "distractors": [
                "improved distractor 1",
                "improved distractor 2",
                "improved distractor 3"
            ]
        },
        "explanation": "what was changed and why"
    }
    """)
    
    DIFFICULTY = Template("""
    As an AP assessment expert, adjust this question's difficulty:
    
    Question: ${question}
    Responses: ${responses}
    Current Difficulty: ${current_difficulty}
    Target Difficulty: ${target_difficulty}
    QC Feedback: ${feedback}
    
    Requirements:
    - Maintain content alignment
    - Use appropriate Bloom's taxonomy verbs
    - Adjust complexity without changing topic
    - Keep question answerable
    
    Format response as JSON:
    {
        "revised_question": "adjusted question",
        "revised_responses": {
            "correct": "adjusted correct answer",
            "distractors": [
                "adjusted distractor 1",
                "adjusted distractor 2",
                "adjusted distractor 3"
            ]
        },
        "explanation": "how difficulty was adjusted"
    }
    """)
