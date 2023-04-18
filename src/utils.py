"""
stuff that doesn't belong in the main file
"""
from datetime import timedelta


def milliseconds_from_time_in_seconds(float_number):
    """
    Example: 1.34 -> 340
    """
    return f'{float_number - int(float_number):.3f}'.split('.')[1]


def format_float_to_time(time_as_float):
    """
    81.34 -> 00:01:21,340
    """
    return '0' + str(timedelta(seconds=int(time_as_float))) \
        + "," + milliseconds_from_time_in_seconds(time_as_float)
