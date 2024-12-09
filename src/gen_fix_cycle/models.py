"""Data models for the gen-fix cycle system."""

from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional, Union

class QuestionType(Enum):
    """Types of questions that can be generated."""
    MCQ = auto()
    FRQ = auto()

class Difficulty(Enum):
    """Question difficulty levels."""
    READING_COMPREHENSION = 0  # Info explicitly stated
    RECALL = 1                 # Related to Bloom's Easy
    ANALYZE = 2                # Related to Bloom's Moderate
    EVALUATE = 3               # Related to Bloom's Difficult

@dataclass
class Response:
    """A response option for a question."""
    text: str
    is_correct: bool
    explanation: Optional[str] = None

@dataclass
class Question:
    """A question with its responses and metadata."""
    text: str
    responses: List[Response]
    question_type: QuestionType
    difficulty: Difficulty
    ek_code: Optional[str] = None  # Essential Knowledge code
    lo_code: Optional[str] = None  # Learning Objective code
    skill_code: Optional[str] = None

@dataclass
class QCResult:
    """Result of a quality check on a question."""
    score: int  # 0 or 1
    rationale: str
    feedback: str
    revised_content: Optional[str] = None

@dataclass
class GenerationCycle:
    """Represents a complete generation cycle for a question."""
    original_question: Question
    qc_results: List[QCResult]
    final_question: Optional[Question] = None
    status: str = "pending"  # pending, needs_revision, complete

    def needs_revision(self) -> bool:
        """Check if any QC checks failed."""
        return any(result.score == 0 for result in self.qc_results)

    def get_failed_checks(self) -> List[QCResult]:
        """Get list of failed QC checks."""
        return [result for result in self.qc_results if result.score == 0]

# JSON Response Schemas
class ResponseSchemas:
    """Standard JSON response schemas for LLM interactions."""
    
    BASIC = {
        "score": "0 or 1",
        "rationale": "2-line explanation",
        "feedback": "2-line feedback"
    }
    
    ALIGNMENT = {
        "score": "0 or 1",
        "rationale": "2-line explanation",
        "ek_aligned": "aligned EK code",
        "lo_aligned": "aligned LO code",
        "skill_aligned": "aligned skill code"
    }
    
    DIFFICULTY = {
        "score": "0 or 1",
        "rationale": "2-line explanation",
        "difficulty": "0, 1, 2, or 3",
        "question_type": "reading_comprehension, recall, analyze, evaluate"
    }
    
    GENERATION = {
        "text": "question text",
        "correct_answer": "correct answer text",
        "distractors": ["distractor1", "distractor2", "distractor3"],
        "explanation": "why this is correct",
        "ek_code": "relevant code",
        "lo_code": "relevant code"
    }

# Course to Subject Mapping
COURSE_MAPPING: Dict[str, List[str]] = {
    "soc": ["APCGOV", "APAPUSGOV", "APHUMG", "APUSH", "APWORLD", "APEURO"],
    "ssc": ["APMACRO", "APMICRO", "APPSYCH"],
    "sci": ["APBIO", "APCHEM", "APENVS", "APPHY1", "APPHY2", "APPHYCEM", "APPHYCMEC"],
    "eng": ["APLANG", "APLIT"],
    "mat": ["APCALCAB", "APCALCBC", "APPRECALC", "APSTAT"],
    "csc": ["APCSCA", "APCSCP"]
}

# Absolute Terms and Pattern Phrases to Avoid
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
