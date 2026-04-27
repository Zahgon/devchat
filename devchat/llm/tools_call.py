import json
import os
import sys
from functools import wraps

from devchat.chatmark import Form, Radio, TextEditor
from devchat.ide import IDEService
from devchat.memory import ChatMemory

from .openai import chat_call_completion_stream


class MissToolsFieldException(Exception):
    pass


def openai_tool_schema(name, description, parameters, required):
    pass


def openai_function_schema(name, description, properties, required):
    pass


def llm_func(name, description, schema_fun=openai_tool_schema):
    pass


def llm_param(name, description, dtype, **kwargs):
    pass


def call_confirm(response):
    """
    Prompt the user to confirm if a function call should be allowed.

    This function is responsible for asking the user to confirm whether the AI's
    intention to call a function is permissible. It prints out the response content
    and the details of the function calls that the AI intends to make. The user is
    then presented with a choice to either allow or deny the function call.

    Parameters:
    response (dict): A dictionary containing the 'content' and 'all_calls' keys.
                     'content' is a string representing the AI's response, and
                     'all_calls' is a list of dictionaries, each representing a
                     function call with 'function_name' and 'parameters' keys.

    Returns:
    tuple: A tuple containing a boolean and a string. The boolean indicates whether
           the function call is allowed (True) or not (False). The string contains
           additional input from the user if the function call is not allowed.
    """
    pass


def chat_tools(
    prompt,
    memory: ChatMemory = None,
    model: str = os.environ.get("LLM_MODEL", "gpt-3.5-turbo-1106"),
    tools=None,
    call_confirm_fun=call_confirm,
    **llm_config,
):
    pass
