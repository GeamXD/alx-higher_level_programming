#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for cha in my_string:
        if cha.lower() == 'c':
            continue
        else:
            new_string += cha
    return new_string
