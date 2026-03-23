"""
https://www.codewars.com/kata/52fba66badcd10859f00097e

Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the
threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.
"""


def disemvowel(s: str) -> str:
    for char in s:
        if char in "aeiouAEIOU":
            s = s.replace(char, "")
    return s


if __name__ == "__main__":
    assert disemvowel("This website is for losers LOL!") == "Ths wbst s fr lsrs LL!"
    assert (
        disemvowel("No offense but,\nYour writing is among the worst I've ever read")
        == "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd"
    )
    assert disemvowel("What are you, a communist?") == "Wht r y,  cmmnst?"
