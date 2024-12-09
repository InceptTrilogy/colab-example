"""Subject-specific criteria for question generation and evaluation."""

from typing import Dict, Optional

class SubjectCriteria:
    """Criteria organized by subject."""
    
    SOCIAL_SCIENCES = {
        "question": """
        - Relates to one or more ek_codes
        - Contains task verbs from LOs if present
        - Can be answered from article or critical thinking
        - Can be answered in 1-2 short sentences
        - Connects concepts to broader themes
        - Provides all needed information
        - Has single clear interpretation
        - Makes only one connection (no multiple 'and's)
        """,
        "correct": """
        - Factually correct
        - One sentence up to 20 words
        - Responds to all question parts
        - Uses task verb correctly
        """,
        "distractor": """
        - Avoids absolute terms
        - Similar length to correct answer
        - Same structure as correct answer
        - Responds to all question parts
        - Related to time period/topic
        - Clearly incorrect but plausible
        """
    }

    SCIENCES = {
        "question": """
        - Relates to specific scientific concepts
        - Uses precise scientific terminology
        - Can be answered through analysis or application
        - Requires understanding of scientific principles
        - Connects to experimental or observational evidence
        - Provides necessary context and data
        """,
        "correct": """
        - Scientifically accurate
        - One sentence up to 20 words
        - Uses precise terminology
        - Shows clear reasoning
        """,
        "distractor": """
        - Based on common misconceptions
        - Uses correct terminology
        - Plausible but incorrect
        - Similar complexity to correct answer
        - Related to core concepts
        """
    }

    # Mapping of subjects to their criteria
    MAPPING = {
        "soc": SOCIAL_SCIENCES,
        "sci": SCIENCES,
        # Add other subjects as needed
    }

def get_criteria(subject: str, criteria_type: str) -> str:
    """Get subject-specific criteria.
    
    Args:
        subject: Subject code (e.g., 'soc', 'sci')
        criteria_type: Type of criteria ('question', 'correct', 'distractor')
    
    Returns:
        Criteria string for the given subject and type
    """
    criteria_dict = SubjectCriteria.MAPPING.get(subject, {})
    return criteria_dict.get(criteria_type, "")
