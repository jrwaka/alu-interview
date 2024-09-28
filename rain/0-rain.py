#!/usr/bin/python3
"""
This module determines the volume of rainwater that can be stored after rainfall.
"""

def rain(walls):
    """
    Compute the number of square units of water that will be trapped post-rainfall.

    Parameters:
    walls -- a list of non-negative integers representing the heights of walls.

    Returns:
    The total amount of rainwater stored as an integer.
    """
    if not walls:
        return 0

    left, right = 0, len(walls) - 1
    left_max, right_max = 0, 0
    water = 0

    while left < right:
        if walls[left] <= walls[right]:
            left_max = max(left_max, walls[left])
            water += left_max - walls[left]
            left += 1
        else:
            right_max = max(right_max, walls[right])
            water += right_max - walls[right]
            right -= 1

    return water
