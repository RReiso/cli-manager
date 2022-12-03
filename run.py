from menu_items import MENU_ITEMS
from menu import Menu
from colors import bcolors

print(f"{bcolors.YELLOW}Welcome to your personal manager app!\n")
menu = Menu()
menu.run(MENU_ITEMS)
