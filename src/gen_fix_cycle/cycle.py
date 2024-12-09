"""Main orchestration for the generation-fix cycle."""

from dataclasses import dataclass
import logging
from typing import List, Optional

from .config import LLMConfig
from .llm import LLMClient, parse_question_response
from .models import Question, QCResult, GenerationCycle, Difficulty
from .prompts.gen import get_generation_prompt
from .prompts.qc import QualityChecker
from .prompts.fix import QuestionFixer
from .prompts.criteria import get_criteria
from .config import get_subject

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class CycleConfig:
    """Configuration for a generation cycle."""
    course: str
    article: str
    ek_codes: Optional[List[str]] = None
    lo_codes: Optional[List[str]] = None
    target_difficulty: Difficulty = Difficulty.ANALYZE
    llm_config: LLMConfig = LLMConfig()

class GenerationCycleManager:
    """Manages the complete generation-fix cycle for questions."""
    
    def __init__(self, config: CycleConfig):
        self.config = config
        self.subject = get_subject(config.course)
        if not self.subject:
            raise ValueError(f"Unknown course: {config.course}")
            
        self.llm = LLMClient(config.llm_config)
        self.qc = QualityChecker(self.llm)
        self.fixer = QuestionFixer(self.llm)
        
    def generate_question(self) -> Question:
        """Generate initial question and responses."""
        logger.info("Generating initial question")
        
        prompt = get_generation_prompt(
            'mcq',
            article=self.config.article,
            ek_codes=self.config.ek_codes,
            lo_codes=self.config.lo_codes,
            criteria=get_criteria(self.subject, 'question'),
            difficulty=self.config.target_difficulty.value
        )
        
        response = self.llm.complete(prompt)
        return parse_question_response(response)
        
    def run_cycle(self) -> GenerationCycle:
        """Run a complete generation-fix cycle."""
        logger.info("Starting generation cycle")
        
        question = self.generate_question()
        cycle = GenerationCycle(
            original_question=question,
            qc_results=[]
        )
        
        qc_results = self.qc.run_all_checks(
            question=question,
            article=self.config.article
        )
        cycle.qc_results = qc_results
        
        if cycle.needs_revision():
            logger.info("Question needs revision")
            fixed_question = self.fixer.fix_question(question, qc_results)
            if fixed_question:
                cycle.final_question = fixed_question
                cycle.status = "complete"
            else:
                cycle.status = "failed"
        else:
            logger.info("Question passed QC")
            cycle.final_question = question
            cycle.status = "complete"
            
        return cycle

def run_generation(config: CycleConfig) -> GenerationCycle:
    """Run a generation cycle with the given configuration."""
    manager = GenerationCycleManager(config)
    return manager.run_cycle()
