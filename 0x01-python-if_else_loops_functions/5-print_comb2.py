#!/usr/bin/python3
for i in range(100):
    first_digit = i // 10
    last_digit = i % 10
    if i < 99:
        print(f"{first_digit:d}{last_digit:d}", end=", ")
    else:
        print(f"{first_digit:d}{last_digit:d}")
