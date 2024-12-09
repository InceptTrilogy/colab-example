"""Configuration for the gen-fix cycle system."""

from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class LLMConfig:
    """Configuration for LLM interactions."""
    model: str = "gpt-4"  # Default to GPT-4 for high quality responses
    temperature: float = 0.2  # Low temperature for consistent, focused responses
    max_tokens: int = 2048
    top_p: float = 0.95
    presence_penalty: float = 0.0
    frequency_penalty: float = 0.0

# Course to subject mapping
COURSE_MAPPING: Dict[str, List[str]] = {
    "soc": ["APCGOV", "APAPUSGOV", "APHUMG", "APUSH", "APWORLD", "APEURO"],
    "ssc": ["APMACRO", "APMICRO", "APPSYCH"],
    "sci": ["APBIO", "APCHEM", "APENVS", "APPHY1", "APPHY2", "APPHYCEM", "APPHYCMEC"],
    "eng": ["APLANG", "APLIT"],
    "mat": ["APCALCAB", "APCALCBC", "APPRECALC", "APSTAT"],
    "csc": ["APCSCA", "APCSCP"]
}

# Bloom's taxonomy levels
BLOOM_EASY = [
    "Define", "Identify", "List", "State", "Describe", "Explain",
    "Summarize", "Interpret", "Illustrate", "Classify", "Compare",
    "Contrast", "Categorize", "Estimate", "Predict", "Infer"
]

BLOOM_MODERATE = [
    "Analyze", "Calculate", "Demonstrate", "Determine", "Develop",
    "Differentiate", "Examine", "Formulate", "Investigate", "Justify",
    "Organize", "Relate", "Solve", "Support", "Use"
]

BLOOM_DIFFICULT = [
    "Appraise", "Apply", "Argue", "Assess", "Compose", "Conclude",
    "Construct", "Create", "Critique", "Design", "Evaluate", "Generate",
    "Hypothesize", "Invent", "Judge", "Plan", "Produce", "Propose",
    "Recommend", "Revise", "Synthesize", "Validate"
]

# Words to avoid in questions/responses
ABSOLUTES = {
    "all", "always", "never", "solely", "sole", "immediate", "immediately",
    "irrelevant", "complete", "completely", "every", "none", "exclusively",
    "purely", "uniform", "universal"
}

PATTERN_PHRASES = {
    "no significant impact", "minimal impact", "impact was limited",
    "effects were limited", "universal", "perfectly equal",
    "largely irrelevant", "passive victims"
}

def get_subject(course: str) -> Optional[str]:
    """Get the subject area for a given course code."""
    for subject, courses in COURSE_MAPPING.items():
        if course in courses:
            return subject
    return None
