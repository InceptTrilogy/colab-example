"""Question generation and fix cycle system.

This package provides a modular system for generating, evaluating, and fixing
AP exam questions. It breaks down the original monolithic notebook into clean,
maintainable modules.

Package Structure:
    config.py - Configuration and constants
    models.py - Data models and structures
    cycle.py - Main orchestration logic
    prompts/ - Prompt templates and generation
        base.py - Base prompt templates
        criteria.py - Subject-specific criteria
        gen.py - Generation prompts
        qc.py - Quality check prompts
        fix.py - Fix prompts

Example:
    from src.gen_fix_cycle.cycle import CycleConfig, run_generation
    from src.gen_fix_cycle.models import Difficulty

    config = CycleConfig(
        course="APHUMG",
        article="article text...",
        target_difficulty=Difficulty.ANALYZE
    )
    
    result = run_generation(config)
"""

from .cycle import CycleConfig, run_generation
from .models import (
    Question,
    QuestionType,
    Difficulty,
    Response,
    QCResult,
    GenerationCycle
)

__all__ = [
    'CycleConfig',
    'run_generation',
    'Question',
    'QuestionType',
    'Difficulty',
    'Response',
    'QCResult',
    'GenerationCycle'
]
