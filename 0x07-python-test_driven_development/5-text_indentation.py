#!/bin/python3
"""
A Module that prints indentation
"""


def text_indentation(text):
    """
    Prints text indentation
    Args:
        text(str): string of texts
    Returns:
        nothing
    Raises:
        TypeError: text must be a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for ch in range(len(text)):
        if text[ch] in ":?.":
            print("{}".format(text[ch]))
            print("")
        elif text[ch - 1] in ":?." and text[ch] == " ":
            pass
        else:
            print("{}".format(text[ch]), end="")
    else:
        pass
