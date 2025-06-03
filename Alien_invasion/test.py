from dataclasses import dataclass
from typing import NamedTuple

@dataclass

class Cointainer:
    book = {
        "hobit":"J.A.A.T",
        "Książka2":"Author2",
        "Książka3":"Author3",
    }

    menu = ["Pokaż książki"]

    options = len(menu)

information = Cointainer()

class Main:
    @staticmethod
    def show_book(main):
        for key, value in main.items():
            print(key, value)

    def show_menu(menu):
        print()
        for index, item in enumerate(menu, start = 1):
            print(f"{index}. {item}")
        print()
        
Main.show_menu(information.menu)
user_input = int(input("Wybierz opcję: "))
if user_input == 1:
    Main.show_book(information.book)





