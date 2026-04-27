"""
Namespace management for workflows
"""

import os
from pathlib import Path
from typing import Dict, List, Set, Tuple

import oyaml as yaml
import yaml as pyyaml
from pydantic import BaseModel, Extra, Field, ValidationError

from devchat.utils import get_logger

from .path import (
    COMMAND_FILENAMES,
    COMMUNITY_WORKFLOWS,
    CUSTOM_BASE,
    CUSTOM_CONFIG_FILE,
    MERICO_WORKFLOWS,
)

logger = get_logger(__name__)


class CustomConfig(BaseModel):
    namespaces: List[str] = []  # active namespaces ordered by priority

    class Config:
        extra = Extra.ignore


class WorkflowMeta(BaseModel):
    name: str = Field(..., description="workflow name")
    namespace: str = Field(..., description="workflow namespace")
    active: bool = Field(..., description="active flag")
    command_conf: Dict = Field(description="command configuration", default_factory=dict)

    def __str__(self):
        return f"{'*' if self.active else ' '} {self.name} ({self.namespace})"


def _load_custom_config() -> CustomConfig:
    """
    Load the custom config file.
    """
    pass


def get_prioritized_namespace_path() -> List[str]:
    """
    Get the prioritized namespaces.

    priority: custom > merico > community
    """
    pass


def iter_namespace(ns_path: str, existing_names: Set[str]) -> Tuple[List[WorkflowMeta], Set[str]]:
    """
    Get all workflows under the namespace path.

    Args:
        ns_path: the namespace path
        existing_names: the existing workflow names to check if the workflow is the first priority

    Returns:
        List[WorkflowMeta]: the workflows
        Set[str]: the updated existing workflow names
    """
    pass


def main():
    pass


if __name__ == "__main__":
    main()
