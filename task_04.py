#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""More fun with for loops."""


def process_data(data):
    """This gets a sum of numbers in a list and their average.

    Args:
        data (list): A list of numbers.

    Returns:
        Tuple: The sum followed by the average of the given numbers list.

    Examples:

        >>> process_data([4, 5, 6])
        (15, 5.0)

        >>> process_data([1, 4, 4])
        (9, 3.0)
    """
    totalsum = 0
    for items in data:
       totalsum += items
    avg = totalsum/len(data)
    return totalsum, float(avg)


