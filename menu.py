from typing import List


class Menu:
    def __init__(self, options: List[tuple], title: str = None):
        self.options = options
        self.title = title

    def show(self, show_title = False):
        if show_title and self.title is not None:
            print('\n' + '-'*20 + '\n' + self.title + '\n')
        
        for option in self.options:
            number, text = option
            print(f'{number}. {text}')

    def wait_an_option(self, show_menu = False, show_title = False):
        if show_menu:
            self.show(show_title)
        
        chosen_option = input("\nChoose an option: ")

        if self.option_is_valid(chosen_option):
            return int(chosen_option)
        else:
            print('\nChoose a valid option!\n')
            self.show()
            return self.wait_an_option()

    def option_is_valid(self, option):
        return option.isnumeric() and any(valid_option == int(option) for valid_option, _ in self.options)