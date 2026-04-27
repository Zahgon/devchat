import click


@click.command(help="Manage topics")
@click.option(
    "--list", "-l", "list_topics", is_flag=True, help="List topics in reverse chronological order."
)
@click.option("--skip", default=0, help="Skip number of topics before showing the list.")
@click.option("-n", "--max-count", default=100, help="Limit the number of topics to output.")
def topic(list_topics: bool, skip: int, max_count: int):
    """
    Manage topics.
    """
    pass
