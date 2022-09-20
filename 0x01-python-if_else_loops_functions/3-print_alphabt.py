#!/usr/bin/python3
for i in range(97, 123):
    if ord('e') == i:
        continue
    elif ord('q') == i:
        continue
    else:
        print("{}".format(chr(i)), end="")
