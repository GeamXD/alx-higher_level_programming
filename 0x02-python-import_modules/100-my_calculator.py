#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import div, mul, sub, add
    from sys import argv
    operator = ["+", "-", "/", "*"]
    count = len(argv) - 1
    sign = argv[2]
    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b> ")
        exit(1)
    if sign not in operator:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    res = 0
    if sign in operator:
        if sign == "+":
            res = add(a, b)
        elif sign == "-":
            res = sub(a, b)
        elif sign == "*":
            res = mul(a, b)
        else:
            res = div(a, b)
    print("{} {} {} = {}".format(a, sign, b, res))
