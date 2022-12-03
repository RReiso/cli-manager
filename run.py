from menu_items import MENU_ITEMS
from menu import Menu
from colors import bcolors


class Manager:

    def start(self):
        print(f"{bcolors.YELLOW}Welcome to your personal manager app!\n")
        main_menu = Menu(MENU_ITEMS)
        main_menu.show()


my_manager = Manager()
my_manager.start()
