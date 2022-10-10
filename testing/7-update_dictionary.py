#!/bin/python3
def update_dictionary(a_dictionary, key, value):
    for keys in range(len(a_dictionary)):
        if keys == key:
            a_dictionary.update({key: value})
        else:
            a_dictionary.update({key: value})
    return a_dictionary
