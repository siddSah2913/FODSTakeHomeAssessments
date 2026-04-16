"""Write a program to create a function that accepts two integers and displays their sum, difference, product, quotient values."""

def operations(num1, num2):
    print(f"\nSum = {num1 + num2}")
    print(f"Difference = {num1 - num2}")
    print(f"Product = {num1 * num2}")
    print(f"Quotient = {num1 / num2:.2f}")

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    # Calling the function to perform operations
    operations(num1, num2)

# error handling for division by zero
except ZeroDivisionError:
    print("\nError: Division by zero is not allowed.")