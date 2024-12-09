"""Example questions for each subject area."""

SOCIAL_SCIENCE_GOOD = [
    {
        "question": "Which of the following characteristics is currently shared by Switzerland, Canada, and New Zealand?",
        "correct": "Low population-growth rates",
        "distractors": [
            "Primate urban systems",
            "High infant-mortality rates",
            "Membership in the European Union (EU)",
            "More than ten percent of the population involved in sheep farming"
        ],
        "explanation": "Tests understanding of demographic patterns without using absolute terms."
    },
    {
        "question": "Since the 1970s changes in social roles have affected population through which of the following?",
        "correct": "Decreased total fertility rates",
        "distractors": [
            "Increased total fertility rates",
            "Increased death rates",
            "Decreased death rates",
            "Increased infant mortality rates"
        ],
        "explanation": "Tests understanding of demographic change with specific timeframe and clear causation."
    }
]

SOCIAL_SCIENCE_BAD = [
    {
        "question": "In what way did Neo-Confucianism emerge as a response to Buddhism during the Song Dynasty?",
        "responses": [
            "It completely rejected all Buddhist teachings and practices.",
            "It integrated some Buddhist concepts while reinforcing Confucian values.",
            "It promoted atheism as a new belief system among scholars.",
            "It led to widespread persecution of Buddhist monks and temples."
        ],
        "reason": "Uses absolute terms like 'completely' and 'all' in distractors."
    },
    {
        "question": "How did environmental factors affect political structures in native societies?",
        "responses": [
            "Varied climates led to different subsistence strategies.",
            "Frequent volcanic eruptions prompted a unified coalition.",
            "Widespread desertification drove continent-wide assemblies.",
            "Seasonal monsoons standardized government forms."
        ],
        "reason": "Distractors are implausible and too extreme."
    }
]

SCIENCE_GOOD = [
    {
        "question": "Which best explains how water properties contribute to sweating as a cooling mechanism?",
        "correct": "The high heat of vaporization allows heat removal through phase change.",
        "distractors": [
            "The high specific heat capacity allows excess heat absorption.",
            "The high surface tension aids water leaving the body.",
            "The high melting temperature enables solid to liquid transition."
        ],
        "explanation": "Tests understanding of water properties and phase changes without absolute terms."
    }
]

SCIENCE_BAD = [
    {
        "question": "What is the average atomic mass of chlorine given isotopic masses and abundances?",
        "responses": [
            "35.438 amu",
            "34.968 amu",
            "36.000 amu",
            "37.500 amu"
        ],
        "reason": "Missing necessary data (isotopic masses and abundances) to solve."
    }
]

EXAMPLES = {
    "soc": {
        "good": SOCIAL_SCIENCE_GOOD,
        "bad": SOCIAL_SCIENCE_BAD
    },
    "sci": {
        "good": SCIENCE_GOOD,
        "bad": SCIENCE_BAD
    }
}

def get_examples(subject: str, example_type: str) -> list:
    """Get subject-specific examples.
    
    Args:
        subject: Subject code (e.g., 'soc', 'sci')
        example_type: Type of examples ('good', 'bad')
    
    Returns:
        List of example questions for the given subject and type
    """
    subject_examples = EXAMPLES.get(subject, {})
    return subject_examples.get(example_type, [])
