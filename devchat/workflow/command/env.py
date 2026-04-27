"""
Commands for managing the python environment of workflows.
"""

import sys
from pathlib import Path
from typing import List, Optional

import click

from devchat.workflow.env_manager import MAMBA_PY_ENVS, PyEnvManager


def _get_all_env_names() -> List[str]:
    """
    Get all the python env names of workflows.
    """
    pass


@click.command(help="List all the python envs of workflows.", name="list")
def list_envs():
    pass


@click.command(help="Remove a specific workflow python env.")
@click.option(
    "--env-name",
    "-n",
    help="The name of the python env to remove.",
    required=False,
    type=str,
)
@click.option("--all", "all_flag", help="Remove all the python envs of workflows.", is_flag=True)
def remove(env_name: Optional[str] = None, all_flag: bool = False):
    pass


@click.group(help="Manage the python environment of workflows.")
def env():
    pass


env.add_command(list_envs)
env.add_command(remove)
