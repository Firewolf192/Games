import random
import os

from colorama import init, Fore

# init(autoreset = True)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


chance = random.randint(0, 100)


while True:
    print(fr"""
                 _______     
                /       \           
               |         \        
                \                    
                 \                   
                  \                     
                   \              
                    \            
                     \          
                      \        
                       \      
                        \    
                         \  
                          \

        """)


    name1 = input("Podaj imię: ")
    name2 = input("Podaj drugie imię: ")
    clear_screen()






    print(fr"""       
                 _______      _______
                /       \    /       \
               |         \__/         |
                \   Chance for love  /
                 \        {Fore.RED}{chance}{Fore.RESET}{Fore.RED}%{Fore.RESET}       / 
                  \                /          
                   \              /
                    \            /
                     \          /
                      \        /
                       \      /
                        \    /
                         \  /
                          \/

        """)

