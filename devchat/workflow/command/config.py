import json
from pathlib import Path

import click
import oyaml as yaml

from devchat.workflow.path import WORKFLOWS_BASE, WORKFLOWS_CONFIG_FILENAME


@click.command(help="Workflow configuration.", name="config")
@click.option("--json", "in_json", is_flag=True, help="Output in json format.")
def config_cmd(in_json: bool):
    pass
