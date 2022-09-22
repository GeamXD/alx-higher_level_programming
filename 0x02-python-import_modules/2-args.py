#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    count = 0
    for arg in argv:
        if len(argv) == 1:
            print("{} arguments.".format(len(argv) - 1))
        elif count == 0 and len(argv) > 1:
            print("{} arguments:".format(len(argv) - 1))
        elif len(argv) > 1 and count > 0:
            print("{}: {}".format(count, arg))
        count += 1