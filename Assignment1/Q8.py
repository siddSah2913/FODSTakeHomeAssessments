'''8.	Write a program to compute the factorial of a number entered by the user. Ensure the input is a valid positive integer. 
If the user enters anything else, display an error message such as “Invalid input! Please enter a positive integer.”'''

print("\n-----Compute factorial of a number.-----")

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is a valid positive integer
if num < 0:
    print("\nInvalid input! Please enter a positive integer.")
else:
    # Computing the factorial
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"The factorial of {num} is {factorial}.")