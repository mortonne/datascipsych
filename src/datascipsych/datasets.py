"""Access to example datasets."""

from importlib import resources


def get_dataset_file(dataset):
    """Get the path to a dataset file."""
    data_file = resources.files("datascipsych").joinpath(f"data/{dataset}.csv")
    return data_file
