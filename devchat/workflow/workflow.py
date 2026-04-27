import os
import sys
from typing import Dict, List, Optional, Tuple

import oyaml as yaml

from .env_manager import EXTERNAL_ENVS, PyEnvManager
from .namespace import get_prioritized_namespace_path
from .path import COMMAND_FILENAMES
from .schema import RuntimeParameter, WorkflowConfig
from .step import WorkflowStep


class Workflow:
    TRIGGER_PREFIX = "/"
    HELP_FLAG_PREFIX = "--help"

    def __init__(self, config: WorkflowConfig):
        self._config = config

        self._runtime_param = None

    @property
    def config(self):
        pass

    @property
    def runtime_param(self):
        pass

    @staticmethod
    def parse_trigger(user_input: str) -> Tuple[Optional[str], Optional[str]]:
        """
        Check if the user input should trigger a workflow.
        Return a tuple of (workflow_name, the input without workflow trigger).

        User input is considered a workflow trigger if it starts with the Workflow.PREFIX.
        The workflow name is the first word after the prefix.
        """
        pass

    @staticmethod
    def load(workflow_name: str) -> Optional["Workflow"]:
        """
        Load a workflow from the command.yml by name.
        A workflow name is the relative path of command.yml
        to the /workflows dir joined by "."
        e.g
        - "unit_tests": means the command file of the workflow is unit_tests/command.yml
        - "commit.en": means the command file is commit/en/command.yml
        - "pr.review.zh": means the command file is pr/review/zh/command.yml
        """
        pass

    def setup(
        self,
        model_name: Optional[str],
        user_input: Optional[str],
        history_messages: Optional[List[Dict]],
        parent_hash: Optional[str],
    ):
        """
        Setup the workflow with the runtime parameters and env variables.
        """
        pass

    def run_steps(self) -> int:
        """
        Run the steps of the workflow.
        """
        pass

    def get_help_doc(self, user_input: str) -> str:
        """
        Get the help doc content of the workflow.
        """
        pass

    def should_show_help(self, user_input) -> bool:
        pass
