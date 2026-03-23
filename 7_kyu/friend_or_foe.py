"""
https://www.codewars.com/kata/55b42574ff091733d900002f

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure
he's not...

Input = ["Ryan", "Kieran", "Jason", "Yous"]
Output = ["Ryan", "Yous"]

Input = ["Peter", "Stephen", "Joe"]
Output = []

Input strings will only contain letters.
Note: keep the original order of the names in the output.
"""

from typing import NoReturn


def friend(x: list[str]) -> list[str | NoReturn]:
    list_friends = [i for i in x if len(i) == 4]
    return list_friends


if __name__ == "__main__":
    assert friend(["Ryan", "Kieran", "Mark"]) == ["Ryan", "Mark"]
    assert friend(["Ryan", "Jimmy", "abc", "d", "Cool Man"]) == ["Ryan"]
    assert friend(["Jimm", "Cari", "aret", "truehdnviegkwgvke", "sixtyiscooooool"]) == [
        "Jimm",
        "Cari",
        "aret",
    ]
