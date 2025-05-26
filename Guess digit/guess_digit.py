import random
import sys

levels = ["łatwy", "średni", "trudny", "zakończ grę"]

easy = []
medium = []
hard = []

class Generate_Digit():
    def random_digit(self):
        self.test = random.randint(1, 10)
        easy.append(self.test)

    def medium_digit(self):
        self.test2 = random.randint(1, 20)
        medium.append(self.test2)
    
    def high_digit(self):
        self.test3 = random.randint(1, 50)
        hard.append(self.test3)

class Menu():
    def show_levels(self):
        print()
        for index, item in enumerate(levels, start = 1):
            capitalize_item = item.capitalize()
            print(f"{index}. {capitalize_item}")
        print()
    
class Points():
    def __init__(self):
        self.easy = 0
        self.medium = 0
        self.hard = 0
        self.easy_numbeer_of_tries = 5
        self.medium_numbeer_of_tries = 5
        self.hard_numbeer_of_tries = 5
  
class Main(Generate_Digit, Points):
    def __init__(self):
        super().__init__()

    def game_start(self, user_choice):
        if user_choice == 1:
            stage = True
            generate_number.random_digit()

            while stage:
                try:
                    print(f"Liczba prób: {self.easy_numbeer_of_tries}")
                    easy_input = int(input("Wybierz liczbę w przedziale (1-10): "))
                    print(f"Podana liczba: {easy_input}\n")

                except ValueError:
                    print("\nWybrana opcja musi być w zakresie (1-10)\n")
                    continue

                if easy_input in easy:
                    stage = False

                    print()
                    print(f"Gratulacje odgadłeś liczbę :)")
                    print("Wygrywasz grę!")
                    print(f"Odgadnięta liczba: {generate_number.test}")
                    self.easy += 1
                    print(f"Punkty: {self.easy}")
                    easy.clear()

                elif easy_input not in range(1, 11):
                    mistake.check_mistakes(easy_input, generate_number.test)

                else: 
                    mistake.check_higher_digit(easy_input, generate_number.test)
                    mistake.check_lower_digit(easy_input, generate_number.test)
                    self.easy_numbeer_of_tries -= 1

                    if self.easy_numbeer_of_tries == 0:
                        self.easy -= 1

                        print("Nie odgadłeś liczby :(")
                        print("Przegrywasz grę")
                        print(f"Wylosowana liczba: {generate_number.test}")
                        print(f"Punkty: {self.easy}")
                        self.easy_numbeer_of_tries = 5
                        break

                    
        elif user_choice == 2:
            stage = True
            generate_number.medium_digit()

            while stage:
                try:
                    print(f"Liczba prób: {self.medium_numbeer_of_tries}")
                    medium_input = int(input("Wybierz liczbę w przedziale (1-20) "))
                    print(f"Podana liczba: {medium_input}\n")

                except ValueError:
                    print(f"\nWybrana opcja musi być cyfrą w zakresie: (1-20)\n")
                    continue

                if medium_input in medium:
                    stage = False
                    print()
                    print(f"Gratulacje odgadłeś liczbę")
                    print("Wygrywasz grę!")
                    print(f"Odgadnięta liczba: {generate_number.test2}")
                    self.medium += 1
                    print(f"Punkty: {self.medium}")
                    medium.clear()

                elif medium_input not in range(1, 21):
                    mistake.check_mistakes(medium_input, generate_number.test2)
                    
                else: 
                    mistake.check_higher_digit(medium_input, generate_number.test2)
                    mistake.check_lower_digit(medium_input, generate_number.test2)
                    self.medium_numbeer_of_tries -= 1

                    if self.medium_numbeer_of_tries == 0:
                        self.medium -= 1 
                        print("Nie odgadłeś liczby :(")
                        print("Przegrywasz grę")
                        print(f"Wylosowana liczba: {generate_number.test2}")
                        print(f"Punkty: {self.medium}")
                        self.medium_numbeer_of_tries = 5
                        break

        elif user_choice == 3:
            stage = True
            generate_number.high_digit()
            
            while stage:
                try:
                    print(f"Liczba prób: {self.hard_numbeer_of_tries}")
                    high_input = int(input("Wybierz liczbę w przedziale (1-50) "))
                    print(f"Podana liczba: {high_input}\n")

                except ValueError:
                    print(f"\nWybrana opcja musi być cyfrą w zakresie: (1-50)\n")
                    continue

                if high_input in hard:
                    stage = False
                    print()
                    print(f"Gratulacje odgadłeś liczbę")
                    print("Wygrywasz grę!")
                    print(f"Odgadnięta liczba: {generate_number.test3}")
                    self.hard += 1
                    print(f"Punkty: {self.hard}")
                    hard.clear()

                elif high_input not in range(1, 51):
                    mistake.check_mistakes(high_input, generate_number.test3)
                    
                else: 
                    mistake.check_higher_digit(high_input, generate_number.test3)
                    mistake.check_lower_digit(high_input, generate_number.test3)
                    self.hard_numbeer_of_tries -= 1

                    if self.hard_numbeer_of_tries == 0:
                        self.hard -= 1 
                        print("Nie odgadłeś liczby :(")
                        print("Przegrywasz grę")
                        print(f"Wylosowana liczba: {generate_number.test3}")
                        print(f"Punkty: {self.hard}")
                        self.hard_numbeer_of_tries = 5
                        break


        elif user_choice == 4:
            print("\nGra została zakończona\n")
            sys.exit(0)


class Mistakes(Main):
    def check_mistakes(self, user_choice, digit):
        if user_choice < digit or user_choice > digit:
            print("\nTwoja liczba jest po za zasięgiem\n")
    
    def check_higher_digit(self, user_choice, digit):
        if user_choice < digit:
            print("\nWylosowana liczba jest większa od twojej\n")
            
    def check_lower_digit(self, user_choice, digit):
        if user_choice > digit:
            print("\nWylosowana liczba jest mniejsza od twojej\n")
       

show = Menu()
generate_number = Generate_Digit()
game = Main()
mistake = Mistakes()


while True:
    show.show_levels()
    try:
        user_input = int(input("Wybierz poziom trudności: "))

    except ValueError:
        print(f"\nWybrana opcja musi być cyfrą!")

    game.game_start(user_input)


   
    