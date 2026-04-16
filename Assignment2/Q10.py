""" 10.	Create a program to design a dice guessing game with the following specifications:
I. The dice has values from 1 to 6.
II. The program should generate a random value for the dice roll.
III. The player should guess the dice value.
IV. If the guess is correct, show a smiling face.
V. If the guess is off by 1 (e.g., dice = 5, guess = 4), show a neutral face.
 """

import random

# Generating a random value
dice_value = random.randint(1, 6)

# Asking the player to guess the dice value
guess = int(input("Guess the dice value (1-6): "))

# Check if the guess is correct
if guess == dice_value:
    print("Correct guess! 😊")
# Check if the guess is off by 1
elif abs(guess - dice_value) == 1:
    print("Close guess! 😐")
else:
    print(f"Wrong guess! 😞")