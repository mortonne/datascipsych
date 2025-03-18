"""Access to example datasets."""

from importlib import resources
import polars as pl


def get_dataset_file(dataset):
    """Get the path to a dataset file."""
    data_file = resources.files("datascipsych").joinpath(f"data/{dataset}.csv")
    return data_file


def clean_osth(data):
    """Clean the Osth & Fox (2019) dataset."""
    columns = [
        "subj",
        "cycle",
        "phase",
        "trial",
        "type",
        "word1",
        "word2",
        "response",
        "RT",
        "correct",
        "lag",
    ]
    cleaned = data.select(columns).with_columns(
        pl.col("response", "RT", "correct", "lag").replace(-1, None),
        probe_type=pl.col("type").replace({"intact": "target", "rearranged": "lure"}),
    )
    return cleaned
