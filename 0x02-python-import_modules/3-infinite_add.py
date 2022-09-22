#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = 0
    res = 0
    for arg in argv:
        if len(argv) == 0:
            pass
        elif len(argv) > 0 and count > 0:
            res += int(arg)
        count += 1
    print(res)
