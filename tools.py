import os
import subprocess


def clear_console():
    """Function clears the console."""
    if os.name in ('nt', 'dos'):
        subprocess.call("cls")
    elif os.name in ('linux', 'osx', 'posix'):
        subprocess.call("clear")
    else:
        print("\n" * 120)


def is_correct_level(str):
    """The function checks the correctness of the game level (number range from 1 to 3)."""
    try:
        num = int(str)
        if num < 1 or num > 3:
            return False
    except ValueError:
        return False
    return True


def is_correct_letter(str):
    """The function checks the correctness of the letter (only one letter is allowed)."""
    alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    if len(str) == 1 and str in alphabet:
        return True
    else:
        return False


def text_messenger(text_message, is_negative=True):
    """The function return colored message. If is_negative=True the message is red else is green."""
    if is_negative:
        return '\x1b[0;37;41m' + ' ' + text_message + ' ' + '\x1b[0m'
    else:
        return '\x1b[0;30;42m' + ' ' + text_message + ' ' + '\x1b[0m'


def check_win(lives, pattern, masked_word):
    if lives > 0 and pattern == masked_word:
        return True
    elif lives <= 0 and pattern != masked_word:
        return True
    else:
        return False
