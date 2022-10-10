#!/bin/python3
def uniq_add(my_list=[]):
    if len(my_list) == 0:
        return my_list
    new_list = list(set(my_list))
    result = 0
    for val in new_list:
        result += val
    return result
