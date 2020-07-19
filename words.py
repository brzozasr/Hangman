import random

alphabet = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"


def mask_word(word):
    """The function masks the word, changes the letters to the underscore \"_\"."""
    new_word = ""
    for letter in word:
        if letter in alphabet:
            new_word += "_"
        else:
            new_word += letter
    return new_word


def unmask_word(letter, pattern, m_word):
    """This function changes the underscore \"_\" to the letter and True if letter is in word."""
    s_letter = letter.lower()
    s_pattern = pattern.lower()
    is_letter_in_word = False

    new_mask_word = ""
    if s_letter in s_pattern and s_letter not in m_word:
        is_letter_in_word = True
        for (p, w) in zip(pattern, m_word):
            if p.lower() == s_letter:
                w = p
            new_mask_word += w

    return new_mask_word, is_letter_in_word


def random_word(list_level):
    """The function selects a random word from the list"""
    return random.choice(list_level)
