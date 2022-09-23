#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, mul, sub, add
    from sys import argv, exit
    operator = ["+", "-", "/", "*"]
    operator2 = ["/", "-"]
    operator3 = ["+", "*"]
    count = len(argv) - 1
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        exit(1)
    sign = argv[2]
    if sign not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if sign in operator3:
        if sign == "+":
            print("{} {} {} = {}".format(a, sign, b, add(a, b)))
        else:
            print("{} {} {} = {}".format(a, sign, b, mul(a, b)))
    if sign in operator2:
        if sign == "-":
            print("{} {} {} = {}".format(a, sign, b, sub(a, b)))
        else:
            print("{} {} {} = {}".format(a, sign, b, div(a, b)))
