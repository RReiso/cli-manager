from colors import bcolors


class Menu:

    def __init__(self, menu_items):
        self.menu_items = menu_items

    def show(self):
        print(
            f"{bcolors.BLUE}What would you like to do? Enter a number!\n" + bcolors.ENDC)

        for idx, item in enumerate(self.menu_items):
            menu_index = idx + 1
            print(f"{menu_index}. {item.description}")

        choice = ""
        while choice not in range(1, len(self.menu_items) + 1):
            try:
                choice = int(input("\nYour choice: "))
            except ValueError:
                continue

        menu_item_index = choice - 1
        new_task = self.menu_items[menu_item_index]()
        new_task.run()

        if new_task.description != "Return to main menu":
            self.show()
