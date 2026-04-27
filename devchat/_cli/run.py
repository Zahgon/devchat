from typing import List, Optional, Tuple

import click

from devchat.utils import rmtree


@click.command(
    help="The 'command' argument is the name of the command to run or get information about."
)
@click.argument("command", required=False, default="")
@click.option(
    "--list",
    "list_flag",
    is_flag=True,
    default=False,
    help="List all specified commands in JSON format.",
)
@click.option(
    "--recursive",
    "-r",
    "recursive_flag",
    is_flag=True,
    default=True,
    help="List commands recursively.",
)
@click.option(
    "--update-sys",
    "update_sys_flag",
    is_flag=True,
    default=False,
    help="Pull the `sys` command directory from the DevChat repository.",
)
@click.option("-p", "--parent", help="Input the parent prompt hash to continue the conversation.")
@click.option(
    "-r",
    "--reference",
    multiple=True,
    help="Input one or more specific previous prompts to include in the current prompt.",
)
@click.option(
    "-i", "--instruct", multiple=True, help="Add one or more files to the prompt as instructions."
)
@click.option(
    "-c", "--context", multiple=True, help="Add one or more files to the prompt as a context."
)
@click.option("-m", "--model", help="Specify the model to use for the prompt.")
@click.option(
    "--config",
    "config_str",
    help="Specify a JSON string to overwrite the default configuration for this prompt.",
)
def run(
    command: str,
    list_flag: bool,
    recursive_flag: bool,
    update_sys_flag: bool,
    parent: Optional[str],
    reference: Optional[List[str]],
    instruct: Optional[List[str]],
    context: Optional[List[str]],
    model: Optional[str],
    config_str: Optional[str] = None,
):
    """
    Operate the workflow engine of DevChat.
    """
    pass


def __make_files_writable(directory):
    """
    Recursively make all files in the directory writable.
    """
    pass


def _clone_or_pull_git_repo(target_dir: str, repo_urls: List[Tuple[str, str]], zip_urls: List[str]):
    """
    Clone a Git repository to a specified location, or pull it if it already exists.

    :param target_dir: The path where the repository should be cloned.
    :param repo_urls: A list of possible Git repository URLs.
    """
    pass
