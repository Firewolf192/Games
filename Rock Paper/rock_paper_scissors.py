import random
import sys



def newline():
    print()

class Main:
    def __init__(self):
        self.items = ["kamień", "papier", "nożyczki"]

        self.random_item = random.randint(0, 2)
        self.item = self.items[self.random_item]

    def get_user_choice(self):
        newline()
        user_input = input("Wybierz opcję: (kamień, papier, nożyczki): ")
        return user_input
    
    def logic(self):
        newline()
        print("(0) Zakończ grę")
        user_input = self.get_user_choice()

        if user_input == "0":
            sys.exit("\nGra została zakończona\n")

        elif user_input == self.item:
            newline()
            print(f"Komputer podał: {self.item}")
            print("Remis")

        elif user_input == "nożyczki" and self.item == "papier":
            newline()
            print(f"Komputer podał: {self.item}")
            print("Pokonałeś komputera, gratulacje")

        elif user_input == "kamień" and self.item == "nożyczki":
            newline()
            print(f"Komputer podał: {self.item}")
            print("Pokonałeś komputera, gratulacje")

        elif user_input == "papier" and self.item == "kamień":
            newline()
            print(f"Komputer podał: {self.item}")
            print("Pokonałeś komputera, gratulacje")

        else:
            newline()
            print(f"Komputer podał: {self.item}")
            print("Komputer cię pokonał ;)")


while True:
    start = Main()
    start.logic()