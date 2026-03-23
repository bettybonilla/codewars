"""
https://www.codewars.com/kata/542ebbdb494db239f8000046

Given a sequence of items and a specific item in that sequence, return the item immediately following the item
specified. If the item occurs more than once in a sequence, return the item after the first occurrence. This should work
for a sequence of any type.

When the item isn't present or nothing follows it, the function should return nil in Clojure and Elixir, Nothing in
Haskell, undefined in JavaScript, None in Python.

next_item([1, 2, 3, 4, 5, 6, 7], 3) # => 4
next_item(['Joe', 'Bob', 'Sally'], 'Bob') # => "Sally"
"""

from typing import Iterable, Optional


def next_item(sequence: Iterable, target: str | int) -> Optional[str | int]:
    sequence = iter(sequence)
    while sequence:
        try:
            item = next(sequence)
            if item == target:
                return next(sequence)
        except StopIteration:
            return None

    return None


if __name__ == "__main__":
    assert next_item([1, 2, 3, 4, 5, 6, 7, 8], 5) == 6
    assert next_item(["a", "b", "c"], "d") is None
    assert next_item(["a", "b", "c"], "c") is None
    assert next_item("testing", "t") == "e"
    assert next_item(iter(range(1, 30000)), 12) == 13
