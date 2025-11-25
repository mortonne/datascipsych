"""Sample module with some sample functions for data analysis."""

import numpy as np
from scipy import stats


def dprime(trial_type, response):
    """
    Calculate d-prime for recognition memory task responses.

    Args:
      trial_type:
        An iterable with strings, indicating whether each trial is a "target"
        or "lure".
      response:
        An iterable with strings, indicating whether the response on each trial
        was "old" or "new".

    Returns:
      The d-prime measure of recognition accuracy.
    """
    # make sure we have arrays
    trial_type = np.asarray(trial_type)
    response = np.asarray(response)

    # check that labels are as expected
    assert set(trial_type) == set(
        ["target", "lure"]
    ), "trial_type must only contain 'target' and 'lure'"
    assert set(response) == set(
        ["old", "new"]
    ), "response must only contain 'old' and 'new'"
    assert trial_type.shape == response.shape

    # calculate hit rate and false-alarm rate
    hr = np.mean((trial_type == "target") & (response == "old"))
    far = np.mean((trial_type == "lure") & (response == "old"))
    d_prime = stats.norm.ppf(hr) - stats.norm.ppf(far)
    return d_prime


def exclude_fast_responses(response_times, threshold):
    """
    Exclude response times that are too fast.
    
    Args:
      response_times:
        An iterable with response times.
      threshold:
        Threshold for marking response times. Response times less than or equal
        to the threshold will be marked False.
    
    Returns:
      filtered:
        An array with only the included response times.
      is_included:
        A boolean array that is False for responses less than the threshold,
        and True otherwise.
    """
    is_included = response_times <= threshold
    filtered = response_times[is_included]
    return filtered, is_included
