#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
str2 = "and is greater than 5"
str3 = "and is 0"
str4 = "and is less than 6 and not 0"
if number >= 0:
    ld = number % 10
    if ld > 5:
        print(f"{str1} {number} is {ld} {str2}")
    elif 6 > ld > 0:
        print(f"{str1} {number} is {ld} {str4}")
    else:
        print(f"{str1} {number} is {ld} {str3}")
else:
    ld = (-1 * number) % 10
    if 0 < ld < 10:
        print(f"{str1} {number} is -{ld} {str4}")
    elif ld == 0:
        print(f"{str1} {number} is {ld} {str3}")
