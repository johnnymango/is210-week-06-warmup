#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Flipping Lists!"""


def flip_keys(to_flip):
    """This function flips the immutable items in the list.

    Args:
        to_flip (list): A list of immutable items such as string or tuples

    Returns:
        Tuple: The sum followed by the average of the given numbers list.

    Examples:

        >>> flip_keys([(1, 2, 3), 'hello'])
        [(3, 2, 1), 'olleh']
    """
    counter = 0
    for items in to_flip:
        myslices = (items[::-1])
        to_flip[counter] = myslices
        counter += 1
    return to_flip