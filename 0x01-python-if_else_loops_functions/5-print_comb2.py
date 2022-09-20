#!/usr/bin/python3
for i in range(100):
    first_digit = i // 10
    last_digit = i % 10
    if i < 99:
        print("{}{}".format(first_digit, last_digit), end=", ")
    else:
        print("{}{}".format(first_digit, last_digit))
