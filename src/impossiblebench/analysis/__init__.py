"""Analysis tools for ImpossibleBench evaluation results."""

from .data_loader import DataLoader, EvalResult, parse_task_display_name
try:
    from .llm_judge import (
        LLMJudge,
        run_batch_api_binary_evaluation,
        run_batch_api_type_evaluation,
        recover_batch_binary_evaluation,
        recover_batch_type_evaluation,
    )
except ImportError:
    # Allow DataLoader/reporting usage without optional judge dependencies.
    LLMJudge = None
    run_batch_api_binary_evaluation = None
    run_batch_api_type_evaluation = None
    recover_batch_binary_evaluation = None
    recover_batch_type_evaluation = None

__all__ = ["DataLoader", "EvalResult", "parse_task_display_name", "LLMJudge", "run_batch_api_binary_evaluation", "run_batch_api_type_evaluation", "recover_batch_binary_evaluation", "recover_batch_type_evaluation"]