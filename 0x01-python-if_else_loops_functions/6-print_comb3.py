#!/usr/bin/python3
for num1 in range(10):
    for num2 in range(10):
        if num1 < num2 and num1 != num2:
            print(f"{num1}{num2}", end="")
            if num1 != 8:
                print(end=", ")
            if num1 == 8:
                print(end="\n")
