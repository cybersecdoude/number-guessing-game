import random

random_number = random.randint(0, 100)

while True:
    guess = int(input("Guess a number from 0 to 100: "))
    if guess == random_number:  
        print(f"You guessed correctly! The number was {random_number}")
        break
    else:
        if guess > random_number:
            print("Too high!")
        else:
            print("Too low!")

