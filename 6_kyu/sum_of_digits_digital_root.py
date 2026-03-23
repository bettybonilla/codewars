"""
https://www.codewars.com/kata/541c8630095125aba6000c00

Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a
single-digit number is produced. The input will be a non-negative integer.

Examples
    16  -->  1 + 6 = 7
   942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2
"""


# Recursive function
def digital_root(n: int) -> int:
    digital_root_sum = 0
    for i in str(n):
        digital_root_sum += int(i)

    # Base case (exit condition)
    if len(str(digital_root_sum)) == 1:
        return digital_root_sum

    # Recursive case
    return digital_root(digital_root_sum)


# Alternative code
# def digital_root(n: int) -> int:
#     root_num = [int(i) for i in str(n)]
#     digital_root_sum = sum(root_num)
#
#     if len(str(digital_root_sum)) == 1:
#         return sum(root_num)
#
#     while len(str(digital_root_sum)) > 1:
#         root_num.clear()
#         for i in str(digital_root_sum):
#             root_num.append(int(i))
#         digital_root_sum = sum(root_num)
#
#     return digital_root_sum


if __name__ == "__main__":
    assert digital_root(16) == 7
    assert digital_root(942) == 6
    assert digital_root(132189) == 6
    assert digital_root(493193) == 2
