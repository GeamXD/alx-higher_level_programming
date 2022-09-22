#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    for arg in argv:
        if count == 0 and len(argv) - 1 == 0:
            print("{} arguments.".format(len(argv) - 1))
        elif count == 0:
            print("{} arguments:".format(len(argv) - 1))
        else:
            print("{}: {}".format(count, arg))
        count += 1
