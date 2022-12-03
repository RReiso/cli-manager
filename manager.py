from colors import bcolors


class Manager:
    def __init__(self, menu_items):
        self.menu_items = menu_items
        print(self.menu_items)

    def start_manager(self):
        print(f"{bcolors.YELLOW}Welcome to your personal manager app!\n")
        self.show_options()

    def show_options(self):
        print(
            f"{bcolors.BLUE}What would you like to do? Enter a number!\n" + bcolors.ENDC)

        for idx, item in enumerate(self.menu_items):
            menu_index = idx + 1
            print(item)
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
        self.show_options()
