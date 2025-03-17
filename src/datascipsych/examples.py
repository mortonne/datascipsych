"""Module with example functions."""

import numpy as np


def hello():
    """Print a greeting."""
    print("Hello world.")


def ismissing(responses):
    """Check if responses are n/a."""
    return np.asarray(responses) == "n/a"
