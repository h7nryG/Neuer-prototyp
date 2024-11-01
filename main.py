import prototype_two_one as prototype
import textwrap
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
        # os.system('cls') clears the console in windows
    elif os.name == 'posix':
        # os.system('clear') clears the console in linux
        os.system('clear')




def show_prototype_one_section(section_key):
    """
    This function shows the section of the game
    :param section_key:
    :return:
    """
    clear_console()
    section = prototype.chapter[section_key]
    wrapped_section = textwrap.fill(section['content'], width=100)
    # print the number of the section for oversight
    print(f"Abschnitt: {section_key}")
    print(wrapped_section)
    for key, value in section['text_options'].items():
        print(f"{key}: {value}")
    return section['options']

def show_prototype_two_section(section_key):
    """
    This function shows the section of the game
    :param section_key:
    :return:
    """
    clear_console()
    section = prototype.chapter[section_key]
    wrapped_section = textwrap.fill(section['content'], width=100)
    # print the number of the section for oversight
    print(f"Abschnitt: {section_key}")
    print(wrapped_section)
    for key, value in section['text_options'].items():
        print(f"{key}: {value}")
    return section['options']

def get_user_input():
    user_input = input("Wähle deine nächsten Schritte: ")
    return user_input


def init_game():
    """
    This function initializes the game
    :return:
    """
    # start the game from the first section
    current_section = 'abs1'
    # show the section
    while True:
        # show the section
        options = show_prototype_one_section(current_section)
        # get the user input
        user_input = get_user_input()
        # check if the user input is in the options
        if user_input in options:
            # set the current section to the user input
            current_section = options[user_input]
        # check if the user input is q or exit
        # if the user input is q or exit, then quit the game
        elif user_input.lower() == 'q' or user_input.lower() == 'exit':
            break
        else:
            # show the error message
            print("Invalid section number. Please enter a valid section number.")

def init_game_two():
    """
    This function initializes the game
    :return:
    """
    # start the game from the first section
    current_section = 'abs1'
    # show the section
    while True:
        # show the section
        options = show_prototype_two_section(current_section)
        # get the user input
        user_input = get_user_input()
        # check if the user input is in the options
        if user_input in options:
            # set the current section to the user input
            current_section = options[user_input]
        # check if the user input is q or exit
        # if the user input is q or exit, then quit the game
        elif user_input.lower() == 'q' or user_input.lower() == 'exit':
            break
        else:
            # show the error message
            print("Invalid section number. Please enter a valid section number.")


def choose_paths():
    """
    This function lets the user choose the path either prototype or the default path
    :return:
    """
    print("Willkommen zu unserem Textadventure!")
    print("Für beenden drücke q oder exit")
    user_choice_path = input("Wähle deinen Pfad: \n1.Individueller Pfad\n2.Standard Pfad\nAuswahl: ")
    if user_choice_path == "1":
        # start the game
        init_game()
    elif user_choice_path == "2":
        # start the game
        init_game_two()
    elif user_choice_path == "q" or user_choice_path == "exit":
        return
    else:
        print("Invalid input. Please enter a valid input.")
        # recursively call the function until the user enters a valid input
        choose_paths()


def main():
    print("\n")
    choose_paths()


if __name__ == "__main__":
   main()
