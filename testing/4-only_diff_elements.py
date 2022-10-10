#!/bin/python3
def only_diff_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return "None"
    new = [unique for unique in set_1 if unique not in set_2] + [uni_x for uni_x in set_2 if uni_x not in set_1]
    return new
