import os

current_dir = os.path.dirname(os.path.realpath(__file__))
file = "countries-and-capitals.txt"
data_file = os.path.join(current_dir, file)


def words_pool():
    tmp_list = []
    list_easy = []
    list_medium = []
    list_hard = []
    if os.path.exists(data_file):
        with open(data_file, "r") as countries_capitals_file:
            for country_capital in countries_capitals_file:
                country_capital = country_capital.strip(os.linesep)
                tmp_list.append(country_capital)
    else:
        print(f"The file \"{data_file}\" doesn't exist!")

    for city in tmp_list:
        dl = len(city)
        if 10 <= dl <= 17:  # length between 10 and 17 characters
            list_easy.append(city)
        elif 18 <= dl <= 24:  # length between 18 and 24 characters
            list_medium.append(city)
        else:  # length greater then 24 characters
            list_hard.append(city)

    tmp_list.clear()

    return list_easy, list_medium, list_hard


def level_name(no):
    name = ""
    if no == 1:
        name = "EASY"
    elif no == 2:
        name = "MEDIUM"
    elif no == 3:
        name = "HARD"

    return name
