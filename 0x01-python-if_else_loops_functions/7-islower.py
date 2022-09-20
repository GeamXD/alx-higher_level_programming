#!/usr/bin/python3
def islower(c):
    for alp in range(97, 123):
        if alp == ord(c):
            return True
    else:
        return False
