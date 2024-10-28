import individual
import content
import textwrap
import os

def clear_console():
    if os.name == 'nt':
        os.system('cls')
        # wenn es nicht windows ist, dann wird es als posix erkannt
    elif os.name == 'posix':
        # wenn die variable TERM in os.environ ist, dann wird es als clear erkannt
        os.system('clear')

def show_default_section():
    """
    This function shows the default path of the game
    :return:
    """
    section_read = 0
    total_sections = len(content.erster_prototyp_pfad)
    for contents in content.erster_prototyp_pfad:
        wrapped_section = textwrap.fill(contents, width=100)
        print(wrapped_section)
        section_read += 1
        print(f"Progress: {section_read / total_sections * 100:.2f}%")
        print("\n")
        input("Press Enter to continue...")


def show_section(section_key):
    """
    This function shows the section of the game
    :param section_key:
    :return:
    """
    clear_console()
    section = individual.chapter[section_key]
    wrapped_section = textwrap.fill(section['content'], width=100)
    print(wrapped_section)
    for key, value in section['text_options'].items():
        print(f"{key}: {value}")
    return section['options']


def get_user_input():
    """
    This function gets the user input
    :return:
    """
    return input("Wähle deine nächsten Schritte: ")


def init_game():
    """
    This function initializes the game
    :return:
    """
    current_section = 'abs1'
    while True:
        options = show_section(current_section)
        user_input = get_user_input()

        if user_input in options:
            current_section = options[user_input]
        else:
            print("Invalid section number. Please enter a valid section number.")


def choose_paths():
    """
    This function lets the user choose the path either individual or the default path
    :return:
    """
    user_choice_path = input("Wähle deinen Pfad: \n1.Individueller Pfad\n2.Standard Pfad\nAuswahl: ")
    if user_choice_path == "1":
        init_game()
    elif user_choice_path == "2":
        show_default_section()
    else:
        print("Invalid input. Please enter a valid input.")
        choose_paths()


def main():
    print("\n")
    choose_paths()


if __name__ == "__main__":
   main()
