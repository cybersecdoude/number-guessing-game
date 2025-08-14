import random

def game_menu():
    print("""
==============================================
    WELCOME TO THE NUMBER GUESSING GAME
==============================================
    Press 1 to Start a New Game
    Press 2 to Exit the Game
==============================================
    """)

def game_credits():
    print("""
==============================================
    THANK YOU FOR PLAYING! GOODBYE :)
    *** Game created by cybersecdoude ***
==============================================
    """)

def number_guessing_game():
    
    random_number = random.randint(0, 100)
    num_of_guesses = 0

    while True:
        
        try:
            guess = int(input("Guess a number from 0 to 100: "))
        except ValueError:
            print("You entered an invalid number, please try again.")
            continue
        num_of_guesses += 1
        
        if guess == random_number:  
            print(f"You guessed correctly after {num_of_guesses} attempt(s)! The number was {random_number}")
            break
        else:
            if guess > random_number:
                print("Too high!")
            else:
                print("Too low!")

game_menu()

while True:

    try:
        start_input = int(input("Select an option: "))
    except ValueError:
        print("Please enter a valid option!")
        continue

    if start_input == 1:
        number_guessing_game()
        game_menu()
    elif start_input == 2:
        game_credits()
        break
    else:
        print("Please enter a valid option!")
