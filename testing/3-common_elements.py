#!/bin/python3
def common_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return "none"
    new_list = [common_x for common_x in set_1 for common_y in set_2 if common_x == common_y]
    return new_list
