import json
import os
import shlex
import subprocess
import sys
import threading
from enum import Enum
from typing import Dict, List, Tuple

from .path import WORKFLOWS_BASE
from .schema import RuntimeParameter, WorkflowConfig


class BuiltInVars(str, Enum):
    """
    Built-in variables within the workflow step command.
    """

    devchat_python = "$devchat_python"
    command_path = "$command_path"
    user_input = "$input"
    workflow_python = "$workflow_python"


class BuiltInEnvs(str, Enum):
    """
    Built-in environment variables for the step subprocess.
    """

    llm_model = "LLM_MODEL"
    parent_hash = "PARENT_HASH"
    context_contents = "CONTEXT_CONTENTS"


class WorkflowStep:
    def __init__(self, **kwargs):
        """
        Initialize a workflow step with the given configuration.
        """
        self._kwargs = kwargs

    @property
    def command_raw(self) -> str:
        """
        The raw command string from the config.
        """
        pass

    def _setup_env(self, wf_config: WorkflowConfig, rt_param: RuntimeParameter) -> Dict[str, str]:
        """
        Setup the environment variables for the subprocess.
        """
        pass

    def _validate_and_interpolate(
        self, wf_config: WorkflowConfig, rt_param: RuntimeParameter
    ) -> List[str]:
        """
        Validate the step configuration and interpolate variables in the command.

        Return the command parts as a list of strings.
        """
        pass

    def run(self, wf_config: WorkflowConfig, rt_param: RuntimeParameter) -> Tuple[int, str, str]:
        """
        Run the step in a subprocess.

        Returns the return code, stdout, and stderr.
        """
        pass
