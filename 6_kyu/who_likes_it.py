"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362

You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other
items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display
text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

Note: For 4 or more names, the number in "and 2 others" simply increases.
"""

from typing import NoReturn


def likes(names: list[str | NoReturn]) -> str:
    if len(names) == 1:
        return f"{names[0]} likes this"

    if len(names) == 2:
        return f"{names[0]} and {names[1]} like this"

    if len(names) == 3:
        return f"{names[0]}, {names[1]} and {names[2]} like this"

    if len(names) >= 4:
        return f"{names[0]}, {names[1]} and {len(names) - 2} others like this"

    return "no one likes this"


if __name__ == "__main__":
    assert likes([]) == "no one likes this"
    assert likes(["Peter"]) == "Peter likes this"
    assert likes(["Jacob", "Alex"]) == "Jacob and Alex like this"
    assert likes(["Max", "John", "Mark"]) == "Max, John and Mark like this"
    assert (
        likes(["Alex", "Jacob", "Mark", "Max"]) == "Alex, Jacob and 2 others like this"
    )
