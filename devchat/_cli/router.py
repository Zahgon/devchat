import json
import sys
from typing import List, Optional

from devchat.workflow.workflow import Workflow


def _get_model_and_config(model: Optional[str], config_str: Optional[str]):
    pass


def _load_tool_functions(functions: Optional[str]):
    pass


def _load_instruction_contents(content: str, instruct: Optional[List[str]]):
    pass


def before_prompt(
    content: Optional[str],
    parent: Optional[str],
    reference: Optional[List[str]],
    instruct: Optional[List[str]],
    context: Optional[List[str]],
    model: Optional[str],
    config_str: Optional[str] = None,
    functions: Optional[str] = None,
    function_name: Optional[str] = None,
    not_store: Optional[bool] = False,
):
    pass


def llm_prompt(
    content: Optional[str],
    parent: Optional[str],
    reference: Optional[List[str]],
    instruct: Optional[List[str]],
    context: Optional[List[str]],
    model: Optional[str],
    config_str: Optional[str] = None,
    functions: Optional[str] = None,
    function_name: Optional[str] = None,
    not_store: Optional[bool] = False,
):
    pass


def llm_commmand(
    content: Optional[str],
    parent: Optional[str],
    reference: Optional[List[str]],
    instruct: Optional[List[str]],
    context: Optional[List[str]],
    model: Optional[str],
    config_str: Optional[str] = None,
):
    pass


def llm_route(
    content: Optional[str],
    parent: Optional[str],
    reference: Optional[List[str]],
    instruct: Optional[List[str]],
    context: Optional[List[str]],
    model: Optional[str],
    config_str: Optional[str] = None,
    auto: Optional[bool] = False,
):
    pass
