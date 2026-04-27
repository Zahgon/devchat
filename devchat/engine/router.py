import os
from typing import List

from .command_runner import CommandRunner
from .namespace import Namespace
from .recursive_prompter import RecursivePrompter
from .util import CommandUtil


def load_workflow_instruction(user_input: str):
    pass


def run_command(
    model_name: str, history_messages: List[dict], input_text: str, parent_hash: str, auto_fun: bool
):
    """
    load command config, and then run Command
    """
    pass
