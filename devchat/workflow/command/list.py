import json
from typing import List

import click

from devchat.utils import get_logger
from devchat.workflow.namespace import (
    WorkflowMeta,
    get_prioritized_namespace_path,
    iter_namespace,
)

logger = get_logger(__name__)


@click.command(help="List all local workflows.", name="list")
@click.option("--json", "in_json", is_flag=True, help="Output in json format.")
def list_cmd(in_json: bool):
    pass
