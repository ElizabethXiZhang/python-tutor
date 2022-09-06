# Shift Items 2
#
# Implement a function that can shift all of the integers of a
# 2D list with a given list of biases.
#
# [Example 1]
# Input:
# _list = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
# biases = [1, 2, 3]
# Output:
# [[2, 3, 4], [3, 4, 5], [4, 5, 6]]
#
# [Example 2]
# Input:
# _list = [[], [2, 1], [-17, 20000000, 1, 1]]
# biases = [3, 0, -20000000]
# Output:
# [[], [2, 1], [-20000017, 0, -19999999, -19999999]]

from typing import List

_list = [[], [2, 1], [-17, 20000000, 1, 1]]
biases = [3, 0, -20000000]
def shift_items(_list: List[List[int]], biases: List[int]) -> List[List[int]]:


        for anchor in range(len(biases)):
            print(_list[anchor])
            print(biases[anchor])
            for item in _list[anchor]:
                #print(item, "+", biases[anchor])
                print(item + biases[anchor])
    
shift_items(_list, biases)
