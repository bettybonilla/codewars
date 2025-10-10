"""
https://www.codewars.com/kata/57f781872e3d8ca2a000007e

Given an array of integers, return a new array with each value doubled.

For example:
[1, 2, 3] --> [2, 4, 6]
"""

from typing import NoReturn


def maps(a: list[int]) -> list[int | NoReturn]:
    if not a:
        return []
    return [i * 2 for i in a]
