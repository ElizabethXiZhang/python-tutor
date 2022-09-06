# Pick Odd Numbers
#
# Implement a function that can collect all of odd numbers from
# a input list without duplicated.
#
# [Example 1]
# Input:
# _list = [1, 2, 3]
# Output:
# [1, 3]
#
# [Example 2]
# Input:
# _list = []
# Output:
# []
#
# [Example 3]
# Input:
# _list = [3, 3, 3, 3, 3, 5, 3]
# Output:
# [3, 5]

from typing import List

_list = [3, 3, 3, 12, 354, 7,  3, 3, 5, 3, 24, 42, 53, 55, 4, 8, 9]
new_list = []
def shift_items(_list: List[int]) -> List[int]:
    for i in _list:
        if  (i % 2) != 0 and i not in new_list:
            new_list.append(i)
    print(new_list)

shift_items(_list)
