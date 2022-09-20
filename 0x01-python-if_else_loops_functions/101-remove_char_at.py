#!/usr/bin/python3
def remove_char_at(str, n):
    output = ""
    count = 0
    for c in str:
        if c:
            if count == n:
                pass
            else:
                output += c
        count += 1
    return output
