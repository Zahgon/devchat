from pathlib import Path

import click

from devchat.workflow.path import (
    WORKFLOWS_BASE,
)
from devchat.workflow.update_util import (
    HAS_GIT,
    copy_workflows_usr,
    update_by_git,
    update_by_zip,
)


@click.command(help="Update the workflow_base dir.")
@click.option("-f", "--force", is_flag=True, help="Force update the workflows to the latest main.")
def update(force: bool):
    pass
