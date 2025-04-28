"""Command line interface functions."""

import sys
import click


def hello():
    """Print a greeting."""
    if len(sys.argv) > 1:
        user = sys.argv[1]
    else:
        user = "world"
    print(f"Hello {user}.")


@click.command()
@click.option("--user", default="world", help="User to greet.")
def hello_click(user):
    print(f"Hello {user}.")
