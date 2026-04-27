"""
Run Command with a input text.
"""

import json
import os
import shlex
import subprocess
import sys
import threading
from typing import Dict, List

from devchat.utils import get_logger

from .command_parser import Command
from .util import ToolUtil

logger = get_logger(__name__)


DEVCHAT_COMMAND_MISS_ERROR_MESSAGE = (
    "devchat-commands environment is not installed yet. "
    "Please install it before using the current command."
    "The devchat-command environment is automatically "
    "installed after the plugin starts,"
    " and details can be viewed in the output window."
)


def pipe_reader(pipe, out_data, out_flag):
    pass


# Equivalent of CommandRun in Python\which executes subprocesses
class CommandRunner:
    def __init__(self, model_name: str):
        self.process = None
        self._model_name = model_name

    def run_command(
        self,
        command_name: str,
        command: Command,
        history_messages: List[Dict],
        input_text: str,
        parent_hash: str,
    ):
        """
        if command has parameters, then generate command parameters from input by LLM
        if command.input is "required", and input is null, then return error
        """
        pass

    def run_command_with_parameters(
        self,
        command_name: str,
        command: Command,
        parameters: Dict[str, str],
        parent_hash: str,
        history_messages: List[Dict],
    ):
        """
        replace $xxx in command.steps[0].run with parameters[xxx]
        then run command.steps[0].run
        """
        pass

    def __run_command_with_thread_output(self, command_str: str, env: Dict[str, str]):
        """
        run command string
        """
        pass

    def __check_command_python_error(self, command_run: str, parameters: Dict[str, str]):
        pass

    def __get_readme(self, command: Command):
        pass

    def __check_input_miss_error(
        self, command: Command, command_name: str, parameters: Dict[str, str]
    ):
        pass

    def __check_parameters_miss_error(self, command: Command, command_run: str):
        # visit parameters in command
        pass

    def __load_command_runtime(self, command: Command):
        pass

    def __load_chat_data(self, model_name: str, parent_hash: str, history_messages: List[Dict]):
        pass

    def __update_devchat_python_path(self, env: Dict[str, str], command_run: str):
        pass

    def _call_function_by_llm(
        self, command_name: str, command: Command, history_messages: List[Dict]
    ):
        """
        command needs multi parameters, so we need parse each
        parameter by LLM from input_text
        """
        pass
