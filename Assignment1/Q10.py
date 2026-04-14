'''10.	Write a number guessing game in Python with the following rules:
    The computer generates a random number between 1 and 50.
    The user must guess the number.
    After each guess, the program tells the user whether the guess is too high, too low, or correct.
    The user gets a maximum of 7 attempts.
    If the user does not guess correctly within the attempts, display “Better luck next time!” and end the game.
'''
import random

print("\n-----Welcome to the Number Guessing Game!-----")

# Generating a random number between 1 and 50
secret_number = random.randint(1, 50)

max_attempts = 7

attempts = 0

# loop through the number of attempts
while attempts < max_attempts:
    # taking input from the user
    guess = int(input("\nGuess a number between 1 and 50: "))
    
    attempts += 1
    
    # Checking if the guess is too high, too low, or correct
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"\nCongratulations!!! You guessed the number in {attempts} attempts.")
        break

# If the user did not guess correctly within the attempts
if attempts == max_attempts:
    print("\n--------------Game Over--------------")
    print(f"\nBetter luck next time!")
