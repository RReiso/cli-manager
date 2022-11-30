from menu_item import MenuItem
from colors import bcolors


class ExitItem(MenuItem):

    @classmethod
    def description(cls):
        return "Exit"

    def run(self):
        print(f"{bcolors.YELLOW}See you next time, bye!")
        exit()
