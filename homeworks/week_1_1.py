# Shift Items
#
# Implement a function that can shift all of the integers of a
# list with a given bias.
#
# [Example 1]
# Input:
# _list = [1, 2, 3]
# bias = 2
# Output:
# [3, 4, 5]
#
# [Example 2]
# Input:
# _list = []
# bias = 10
# Output:
# []

from typing import List

bias = -3
_list = [1,2,3]
def shift_items(_list: List[int], bias: int) -> List[int]:
    return [x+bias for x in _list]
shift_items(_list, bias)
