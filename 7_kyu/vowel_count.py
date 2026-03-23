"""
https://www.codewars.com/kata/54ff3102c1bad923760001f3

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence: str) -> int:
    vowel_count = 0
    for char in sentence:
        if char in "aeiou":
            vowel_count += 1
    return vowel_count


if __name__ == "__main__":
    assert get_count("aeiou") == 5
    assert get_count("y") == 0
    assert get_count("bcdfghjklmnpqrstvwxz y") == 0
    assert get_count("") == 0
    assert get_count("abracadabra") == 5
