"""
https://www.codewars.com/kata/5601409514fc93442500010b

There was a test in your class and you passed it. Congratulations!

But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return true if you're better, else false!

Note:
Your points are not included in the array of your class's points. Do not forget them when calculating the average score!
"""


def better_than_average(class_points: list[int], your_points: int) -> bool:
    total_points = sum(class_points) + your_points
    total_students = len(class_points) + 1
    avg_score = total_points / total_students
    if avg_score < your_points:
        return True

    return False


if __name__ == "__main__":
    assert better_than_average([2, 3], 5)
    assert better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75)
    assert better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69)
