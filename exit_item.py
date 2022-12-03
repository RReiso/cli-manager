from menu_item import MenuItem
from colors import bcolors


class ExitItem(MenuItem):

    description = "Exit"

    def run(self):
        print(f"{bcolors.YELLOW}See you next time, bye!")
        exit()
