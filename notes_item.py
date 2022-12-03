from menu_item import MenuItem
from menu import Menu
from colors import bcolors


class ReadNotesItem(MenuItem):
    description = "Read notes"

    def run(self):
        print(
            f"\n{bcolors.GREEN}Your notes:" + bcolors.ENDC)
        with open("notes.txt", 'r') as notes:
            print(notes.read(), '\n')


class AddNotesItem(MenuItem):
    description = "Add a new note"

    def run(self):
        note = input("Note: ")
        with open("notes.txt", 'a') as notes:
            notes.write("\n" + note)

        print(f"{bcolors.GREEN}Note added!\n" + bcolors.ENDC)


class DeleteNotesItem(MenuItem):
    description = "Delete notes"

    def run(self):
        with open("notes.txt", 'w') as notes:
            notes.write("")
        print(f"{bcolors.GREEN}Notes deleted!\n" + bcolors.ENDC)


class ExitNotesItem(MenuItem):
    description = "Return to main menu"

    def run(self):
        exit


class NotesItem(MenuItem):

    description = "Show Notes menu"

    def __init__(self):
        self.note_items = [ReadNotesItem,
                           AddNotesItem, DeleteNotesItem, ExitNotesItem]

    def run(self):
        notes_menu = Menu()
        notes_menu.run(self.note_items)
