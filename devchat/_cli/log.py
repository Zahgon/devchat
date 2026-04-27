import json
import os
import sys
import time
from dataclasses import dataclass, field
from typing import Dict, List, Optional

import click


@dataclass
class PromptData:
    model: str = "none"
    messages: Optional[List[Dict]] = field(default_factory=list)
    parent: Optional[str] = None
    references: Optional[List[str]] = field(default_factory=list)
    timestamp: int = time.time()
    request_tokens: int = 0
    response_tokens: int = 0


@click.command(help="Process logs")
@click.option("--skip", default=0, help="Skip number prompts before showing the prompt history.")
@click.option("-n", "--max-count", default=1, help="Limit the number of commits to output.")
@click.option(
    "-t",
    "--topic",
    "topic_root",
    default=None,
    help="Hash of the root prompt of the topic to select prompts from.",
)
@click.option("--insert", default=None, help="JSON string of the prompt to insert into the log.")
@click.option("--delete", default=None, help="Hash of the leaf prompt to delete from the log.")
def log(skip, max_count, topic_root, insert, delete):
    """
    Manage the prompt history.
    """
    pass
