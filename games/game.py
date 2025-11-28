import random

def print_menu():
    print("Choose your difficulty level:")
    print("1. Easy (1-10)")
    print("2. Medium (1-100)")  
    print("3. Hard (1-1000)")
    
tries = 10


def choose_diff() -> int:
    level = input("enter 1,2 or 3: ")

    match level:
        case "1":
            return 10
        case "2":
            return 100
        case "3":
            return 1000
        case _:
            print("Choice invalid! Defaulting to hard.")
            return 1000


def game(max_num: int):
    number = random.randint(1, max_num)
    print(f"Guess the number between 1 and {max_num}. You have 10 tries!")  

global tries

    while tries > 0:
        try:
            guess = int(input("Enter number:"))
        except ValueError:
            print("Integer invalid") 
            continue

        tries -= 1
        if guess < number:    
            print("Too low!")   
        elif guess > number:    
            print("Too high!")    
        else:    
            print("Number Guessed.", number)
        break    
    ##error= tries defined


if __name__ == "__main__":
    print_menu()
    diff = choose_diff()
    game(diff) 

    
