import json
import os
import sys
from typing import Dict, List

from devchat._cli.utils import init_dir
from devchat.utils import get_logger

from .command_parser import Command, CommandParser
from .namespace import Namespace

logger = get_logger(__name__)


DEFAULT_MODEL = "gpt-3.5-turbo"


class CommandUtil:
    @staticmethod
    def __command_parser():
        pass

    @staticmethod
    def load_command(command: str):
        pass

    @staticmethod
    def load_commands() -> List[Command]:
        pass


class ToolUtil:
    @staticmethod
    def __make_function_parameters(command: Command):
        pass

    @staticmethod
    def make_function(command: Command, command_name: str):
        pass

    @staticmethod
    def select_function_by_llm(
        history_messages: List[Dict], tools: List[Dict], model: str = DEFAULT_MODEL
    ):
        pass

    @staticmethod
    def _create_tool(command_name: str, command: Command) -> dict:
        pass
