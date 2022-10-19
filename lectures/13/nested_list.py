#
# Notebook 13 - Recursion
#

import doctest

# A nested number list is a lists whose elements are either:
# 1) numbers
# 2) nested number lists

def nested_sum(nested_number_list):
    '''Sum all numbers in a nested number lists.
    Examples:
    >>> nested_sum([1,2,3])
    6
    >>> nested_sum([1, [2,3], 4])
    10
    >>> nested_sum([1, [2], [], [3,4]])
    10
    '''

    total = 0
    for element in nested_number_list:
        if type(element) is list:
            total += nested_sum(element)
        else:
            total += element
    return total
