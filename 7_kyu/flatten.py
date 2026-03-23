"""
https://www.codewars.com/kata/5250a89b1625e5decd000413

Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of
flattening.

flatten([1,2,3])  ==> [1,2,3]
flatten([[1,2,3],["a","b","c"],[1,2,3]])  ==> [1,2,3,"a","b","c",1,2,3]
flatten([[[1,2,3]]])  ==> [[1,2,3]]
"""

from typing import Any


def flatten(lst: list[Any]) -> list[Any]:
    flattened = []
    for i in lst:
        if type(i) is list:
            flattened.extend(i)
        else:
            flattened.append(i)
    return flattened


if __name__ == "__main__":
    assert flatten([]) == []
    assert flatten([1, 2, 3]) == [1, 2, 3]
    assert flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3]]) == [
        1,
        2,
        3,
        "a",
        "b",
        "c",
        1,
        2,
        3,
    ]
    assert flatten([[1, 2, 3], ["a", "b", "c"], [1, 2, 3], "a"]) == [
        1,
        2,
        3,
        "a",
        "b",
        "c",
        1,
        2,
        3,
        "a",
    ]
    assert flatten([[3, 4, 5], [[9, 9, 9]], ["a,b,c"]]) == [3, 4, 5, [9, 9, 9], "a,b,c"]
    assert flatten([[[3], [4], [5]], [9], [9], [8], [[1, 2, 3]]]) == [
        [3],
        [4],
        [5],
        9,
        9,
        8,
        [1, 2, 3],
    ]
