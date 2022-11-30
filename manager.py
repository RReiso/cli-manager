from colors import bcolors
from menu_items import MENU_ITEMS


class Manager:
    # def __init__(self):
    # self.OPTIONS = list(range(1, len(MENU_ITEMS) + 1))

    def start_manager(self):
        print(f"{bcolors.YELLOW}Welcome to your personal manager app!\n")
        self.show_options()

    def show_options(self):
        print(
            f"{bcolors.BLUE}What would you like to do? Enter a number!\n" + bcolors.ENDC)

        for idx, item in enumerate(MENU_ITEMS):
            print(f"{idx + 1}. {item.description()}")

        # for num in self.OPTIONS:
        #     print(f"{num}. {MENU_ITEMS[num - 1].description()}")

        choice = ""
        while choice not in range(1, len(MENU_ITEMS) + 1):
            # while choice not in self.OPTIONS:
            try:
                choice = int(input("\nYour choice: "))
            except ValueError:
                continue

        new_task = MENU_ITEMS[choice - 1]()
        new_task.run()
        self.show_options()


manager = Manager()
manager.start_manager()
