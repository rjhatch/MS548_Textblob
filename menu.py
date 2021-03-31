from formatting import *
from userinput import CaptureTextFromTheUser


class Menu:
    def __init__(self):
        self.menu_items = dict()

    def display_menu(self):
        clear_screen()
        print()
        for val in self.menu_items.keys():
            print(val, ") ", self.menu_items[val].menu_prompt())
        print(len(self.menu_items.keys()) + 1, ") ", "Quit.")

    def add_menu_item(self, name, menu_prompt, descriptive_text, function):
        """Add a menu item.

        Name is the name of the menu item, menu_prompt is what is displayed on the menu,
        descriptive_text is what is passed to the function to display,
        function is the function to call."""
        menu_item = MenuItem(name, menu_prompt, descriptive_text, function)
        self.menu_items[len(self.menu_items) + 1] = menu_item

    def call_menu_item(self, selection):
        try:
            selection = int(selection)
        except:
            print("Please enter a number.")
            input("Press ENTER to continue.")
            return

        if selection > len(self.menu_items) + 1:
            print("Please select a valid option.")
            input("Press ENTER to continue.")
            return

        if selection == len(self.menu_items) + 1:
            print("Goodbye!")
            return "QUIT"

        self.menu_items[selection].function(CaptureTextFromTheUser(self.menu_items[selection].descriptive_text()),
                                            "Hello")


class MenuItem:
    """Create a menu item.

    Name is the name of the menu item, menu_prompt is what is displayed on the menu,
    descriptive_text is what is passed to the function to display,
    function is the function to call."""

    def __init__(self, name, menu_prompt, descriptive_text, function):
        self._name = name
        self._menu_prompt = menu_prompt
        self._descriptive_text = descriptive_text
        self._function = function

    def name(self):
        return self._name

    def menu_prompt(self):
        return self._menu_prompt

    def descriptive_text(self):
        return self._descriptive_text

    def function(self, *args):
        return self._function(*args)
