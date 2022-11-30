from menu_item import MenuItem
from colors import bcolors


class NotesItem(MenuItem):

    @classmethod
    def description(cls):
        return "Show Notes menu"

    def __init__(self):
        self.note_actions = [("Read notes", self.read_notes), ("Add a note", self.add_note),
                             ("Delete notes", self.delete_notes), ("Return to main menu", self.return_to_main_menu)]

    def run(self):
        for idx, action in enumerate(self.note_actions):
            print(f"{idx + 1}. {action[0]}")

        choice = ""
        while choice not in range(1, len(self.note_actions) + 1):
            try:
                choice = int(input("\nYour choice: "))
            except ValueError:
                continue

        self.note_actions[choice - 1][1]()

    def read_notes(self):
        print(
            f"\n{bcolors.GREEN}Your notes:" + bcolors.ENDC)
        with open("notes.txt", 'r') as notes:
            print(notes.read(), '\n')

    def add_note(self):
        note = input("Note: ")
        with open("notes.txt", 'a') as notes:
            notes.write("\n" + note)
        print(f"{bcolors.GREEN}Note added!\n" + bcolors.ENDC)

    def delete_notes(self):
        with open("notes.txt", 'w') as notes:
            notes.write("")
        print(f"{bcolors.GREEN}Notes deleted!\n" + bcolors.ENDC)

    def return_to_main_menu(self):
        exit
