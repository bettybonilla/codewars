"""
https://www.codewars.com/kata/5413759479ba273f8100003d

Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)

Remove this comment otherwise your code cannot pass the anti-cheat tests!

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use " x = list() " instead
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.
"""

from typing import Any


# Reverses a list in place
def reverse(lst: list[Any]) -> list[Any]:
    for index, i in enumerate(range(len(lst))):
        lst.insert(index, lst[-1])
        lst.pop()
    return lst


# def reverse(lst: list[Any]) -> list[Any]:
#     reversed_list = list()
#     for i in range(len(lst)):
#         reversed_list.append(lst.pop())
#     return reversed_list


if __name__ == "__main__":
    assert reverse(list([1, 2, 3])) == [3, 2, 1]
    assert reverse(list([1, None, 14, "two"])) == ["two", 14, None, 1]
