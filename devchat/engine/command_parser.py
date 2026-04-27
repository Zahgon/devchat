import os
from typing import Dict, List, Optional

import oyaml as yaml
from pydantic import BaseModel

from .namespace import Namespace


class Parameter(BaseModel):
    type: str = "string"
    description: Optional[str] = None
    enum: Optional[List[str]] = None
    default: Optional[str] = None


class Command(BaseModel):
    description: str
    hint: Optional[str] = None
    parameters: Optional[Dict[str, Parameter]] = None
    input: Optional[str] = None
    steps: Optional[List[Dict[str, str]]] = None
    path: Optional[str] = None


class CommandParser:
    def __init__(self, namespace: Namespace):
        self.namespace = namespace

    def parse(self, name: str) -> Command:
        """
        Parse a command configuration file to JSON.

        :param name: The command name in the namespace.
        :return: The JSON representation of the command.
        """
        pass


def parse_command(file_path: str) -> Command:
    """
    Parse and validate a YAML configuration file.

    :param file_path: The path to the configuration file.
    :return: The validated configuration as a Pydantic model.
    """
    pass
