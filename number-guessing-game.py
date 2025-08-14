import random

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
