"""
https://www.codewars.com/kata/54da5a58ea159efa38000836

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""

from typing import Optional


def find_it(num_list: list[int]) -> Optional[int]:
    for num in num_list:
        if num_list.count(num) % 2 == 1:
            return num
    return None


if __name__ == "__main__":
    assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
    assert find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
    assert find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
    assert find_it([10]) == 10
    assert find_it([10, 10, 10]) == 10
    assert find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
    assert find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1
