'''This program accepts a list of integers from the user, performs basic arithmetic operations (addition, subtraction, multiplication, 
and division), and saves the results to a file with the current date and time. The program continues until the user decides to exit. 
After exit, it displays the contents of the file.'''

import datetime
# To avoid FileNotFoundError when running the program from a different directory 
import os

# Getting the folder path of current program file and joining it with results.txt
folder_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(folder_path, "results.txt")

# declaring ans variable to control the loop
ans = 'no'

# Loop to continue until the user says yes to exit
while (ans != 'yes'):
    numbers = input("\nEnter a list of integers separated by commas: ")

    # Converting the input string into a list of integers
    numbers = [int(num.strip()) for num in numbers.split(',')]

    addition = sum(numbers)
    subtraction = numbers[0]
    for num in numbers[1:]:
        subtraction -= num

    multiplication = 1
    for num in numbers:
        multiplication *= num

    # Error handling for division by zero
    try:
        division = numbers[0]
        for num in numbers[1:]:
            division /= num
    except ZeroDivisionError:
        print("\nError: Division by zero is not allowed.")
        # Setting division to infinity to show an error in the result
        division = float('inf')

    # Saving the results to a file with the current date and time
    with open(file_path, "a") as f:
        print("-" * 50)
        f.write(f"{datetime.datetime.now().replace(microsecond=0)} :\n Addition: {addition}\n Subtraction: {subtraction}\n Multiplication: {multiplication}\n Division: {division:.2f}\n")

    # Asking the user if they want to exit the program
    ans = input("Do you want to exit the program? (yes/no): ").lower()

if ans == 'yes':
    print("Exiting the program.....\n")
    with open(file_path, "r") as f:    
        print(f.read())
