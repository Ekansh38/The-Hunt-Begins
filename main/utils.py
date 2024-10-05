def is_single_word(s):
    s = s.strip()
    return " " not in s and "\t" not in s and len(s) > 0


import os
import platform


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
