from __future__ import annotations


class PipelineError(RuntimeError):
    """Base error for pipeline runner failures."""


class PipelineContractError(PipelineError):
    """Raised when required pipeline contracts are missing or inconsistent."""


class PipelineCheckpointError(PipelineError):
    """Raised when a checkpoint is missing or malformed."""
