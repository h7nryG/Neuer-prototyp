import prototype_two_one as prototype
import prototype_two_two as prototype_two
import textwrap
import os


def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    elif os.name == 'posix':
        os.system('clear')


def display_section(section_key, prototype_type):
    clear_screen()
    section = prototype_type.chapter[section_key]
    wrapped_section = textwrap.fill(section['content'], width=100)
    print(f"Abschnitt: {section_key}")
    print(wrapped_section)
    for key, value in section['text_options'].items():
        print(f"{key}: {value}")
    return section['options']


def prompt_user_input():
    return input("Wähle deine nächsten Schritte: ")


def start_game(prototype_type):

    current_section = 'abs1'
    while True:
        options = display_section(current_section, prototype_type)
        user_input = prompt_user_input()
        if user_input in options:
            current_section = options[user_input]
        elif user_input.lower() in ['q', 'exit']:
            break
        else:
            print("Invalid section number. Please enter a valid section number.")

    print("Vielen Dank fürs Spielen!")
def select_game_paths():
    print("Willkommen zu unserem Textadventure!")
    print("Für beenden drücke q oder exit")
    user_choice_path = input("Wähle deinen Pfad: \n1. Individueller Pfad\n2. Standard Pfad\n3. Beenden ('q', 'exit',)\nAuswahl: ")
    if user_choice_path == "1":
        start_game(prototype)
    elif user_choice_path == "2":
        start_game(prototype_two)
    elif user_choice_path.lower() in ['q', 'exit']:
        return
    else:
        print("Ungültige Eingabe. Wähle eine gültige Option!")
        select_game_paths()


def main():
    print("\n")
    select_game_paths()


if __name__ == "__main__":
    main()