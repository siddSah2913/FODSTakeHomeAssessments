"""2.	Write a program to implement separate functions for the following mathematical operations. 
Each function should take two user inputs as parameters, operate, and return the result. Display the results clearly with proper formatting.
I. Addition
II. Multiplication
III. Division
IV. Floor Division
V. Exponentiation
"""

# Function for addition
def addition(num1, num2):
    return num1 + num2

# Function for multiplication
def multiplication(num1, num2):
    return num1 * num2

# Function for division
def division(num1, num2):
    return num1 / num2

# Function for floor division
def floor_division(num1, num2):
    return num1 // num2

# Function for exponentiation
def exponentiation(num1, num2):
    return num1 ** num2

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    # Calling the functions and displaying the results
    print(f"\nAddition = {addition(num1, num2)}")
    print(f"Multiplication = {multiplication(num1, num2)}")
    print(f"Exponentiation = {exponentiation(num1, num2)}")
    print(f"Division = {division(num1, num2)}")
    print(f"Floor Division = {floor_division(num1, num2)}")
    
# error handling for division by zero
except ZeroDivisionError:
    print(f"\nError: Division by zero is not allowed.")

