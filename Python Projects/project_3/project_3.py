# Project name - Guess the Number(computer)

import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_number:
            print("Sorry, guess again. Too Low.")
        elif guess > random_number:
            print("Sorry, guess again. Too high.")
        print(guess)
    
    print(f"Yay, congratulations. You have guessed the number {random_number} correctly!!")

number_range = int(input("Choose a range: "))
guess(number_range)