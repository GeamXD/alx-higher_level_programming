#!/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    # method using max()
    # max_key = max(a_dictionary, key=a_dictionary.get)
    # return max_key
    # first make a list of keys to get initial key
    initial_key = list(a_dictionary.keys())[0]
    # then we use the value of our key to get an initial max
    initial_max = a_dictionary[initial_key]
    for key, value in a_dictionary.items():
        if value > initial_max:
            initial_max = value  # we assign initial max to value
            initial_key = key  # we reassign our initial key inorder to return the key we got
    return initial_key
