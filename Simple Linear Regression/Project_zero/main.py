from constant import MENU , OPTIONS
from utility import set_values, find_best_values, loss_function


def menu():
    print(MENU)
    print()
    print(OPTIONS)
    option = input("ENTER YOUR CHOICE: ".rjust(100))
    match option:
        case '1':
            set_values('loss')

menu()
    
    
    
