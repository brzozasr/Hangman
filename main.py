import ascii_art as art
import tools
import level
import words

# DIFFICULTY LEVELS:
# Number of words per level (words length):
# - EASY: characters from 11 to 17 is 85 words, number of lives 9
# - MEDIUM: characters from 18 to 24 is 84 words, number of lives 10
# - HARD: characters from 25 to 47 is 27 words, number of lives 12
list_countries_easy = []
list_countries_medium = []
list_countries_hard = []

# Global variables controlling game status
lives = 0
level_txt = ""
game_level = 0
art_img = 0
pattern = ""
masked_word = ""
wrong_letters = set()
message = ""


def set_lives(new_lives):
    """Setter for the global variable "lives" (number of lives)."""
    global lives
    lives = new_lives


def set_level_txt(new_level_txt):
    """Setter for the global variable "level_txt" (text name level e.g. EASY)."""
    global level_txt
    level_txt = new_level_txt


def set_game_level(new_game_level):
    """Setter for the global variable "game_level" (number of level from 1 to 3)."""
    global game_level
    game_level = new_game_level


def set_art_img(new_art_img):
    """Setter for the global variable "art_img" (ASCI art picture)."""
    global art_img
    art_img = new_art_img


def set_pattern(new_pattern):
    """Setter for the global variable "pattern" (pattern of word)."""
    global pattern
    pattern = new_pattern


def set_masked_word(new_masked_word):
    """Setter for the global variable "masked_word" (keep masked word)."""
    global masked_word
    masked_word = new_masked_word


def set_message(new_message):
    """Setter for the global variable "message" (set message win or lost)."""
    global message
    message = new_message


def set_wrong_letters(letter):
    """Setter for the global variable "wrong_letters" (adding wrong letter to the set)."""
    global wrong_letters
    m_word = masked_word.lower()
    if letter not in m_word:
        wrong_letters.add(letter)


def get_wrong_letters():
    result = ""
    if len(wrong_letters) > 0:
        for letter in wrong_letters:
            result += letter + " "
    result = result.strip()
    return result.replace(" ", ", ")


def clear_game():
    set_lives(0)
    set_level_txt("")
    set_game_level(0)
    set_art_img(0)
    set_pattern("")
    set_masked_word("")
    wrong_letters.clear()
    set_message("")


def set_words_level_pool():
    list_countries_easy.extend(level.words_pool()[0])
    list_countries_medium.extend(level.words_pool()[1])
    list_countries_hard.extend(level.words_pool()[2])


def start_level_setting():
    """Sets the initial game variables."""
    if game_level == 1:                # Easy level
        set_pattern(words.random_word(level.words_pool()[0]))
        set_masked_word(words.mask_word(pattern))
        set_lives(art.art_easy()[1])
        set_level_txt(level.level_name(1))
        set_art_img(art.art_easy()[0][lives])
    elif game_level == 2:              # Medium level
        set_pattern(words.random_word(level.words_pool()[1]))
        set_masked_word(words.mask_word(pattern))
        set_lives(art.art_medium()[1])
        set_level_txt(level.level_name(2))
        set_art_img(art.art_medium()[0][lives])
    elif game_level == 3:              # Hard level
        set_pattern(words.random_word(level.words_pool()[2]))
        set_masked_word(words.mask_word(pattern))
        set_lives(art.art_hard()[1])
        set_level_txt(level.level_name(3))
        set_art_img(art.art_hard()[0][lives])


def update_game_status(letter):
    result = words.unmask_word(letter, pattern, masked_word)
    is_guess = result[1]
    if is_guess:
        set_masked_word(result[0])
        if tools.check_win(lives, pattern, masked_word):
            set_message("You have won!!!")
            tools.text_messenger(message, False)
    else:
        if lives > 0:
            m_word = masked_word.lower()
            if letter not in wrong_letters and letter not in m_word:
                set_lives(lives - 1)
            set_wrong_letters(letter)
            if game_level == 1:
                set_art_img(art.art_easy()[0][lives])
            elif game_level == 2:
                set_art_img(art.art_medium()[0][lives])
            elif game_level == 3:
                set_art_img(art.art_hard()[0][lives])

        if tools.check_win(lives, pattern, masked_word):
            set_message("You have lost!!!")
            tools.text_messenger(message)


def console_printer(no_lives, levels, img, hidden_word, wrong_letter, mess):
    print(f"""
         H A N G M A N
 LIVES: {no_lives}          LEVEL: {levels}
{img}
        {mess}
The word to guess (country - capital city):
    {hidden_word}
You've entered (wrong): {wrong_letter}""")


def main():
    set_words_level_pool()
    is_game_running = True
    while is_game_running:
        if game_level == 0:
            clear_game()
            print("GAME LEVELS: \"1\" - easy, \"2\" - medium, \"3\" - hard or write \"exit\" to terminate the game.")
            input_level = input("Choose the game level: ")
            if input_level == "exit":
                break
            if tools.is_correct_level(input_level):
                set_game_level(int(input_level))
                start_level_setting()
            else:
                continue
        elif 0 < game_level <= 3:
            tools.clear_console()
            console_printer(lives, level_txt, art_img, masked_word, get_wrong_letters(), message)
            print("Write \"exit\" to terminate the game.")
            letter = input("Choose a letter: ")
            letter = letter.lower()
            if letter == "exit":
                break
            elif tools.is_correct_letter(letter):
                update_game_status(letter)
                if message == "You have lost!!!" or message == "You have won!!!":
                    tools.clear_console()
                    console_printer(lives, level_txt, art_img, masked_word, get_wrong_letters(), message)
                    set_game_level(0)


main()
