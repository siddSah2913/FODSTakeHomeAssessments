'''3.	Write a program that prompts the user to enter a number and determines whether it is 
positive, even, positive odd, negative, or negative odd.'''

print("\n-----Check if the number is positive, even, positive odd, negative, or negative odd.-----")

# Taking input from the user
num = int(input("Enter a number: "))

# Checking if the number is positive, even, positive odd, negative, or negative odd
if num > 0:
    if num % 2 != 0:
        print(f"{num} is positive odd.")
    else:
        print(f"{num} is positive.")
        print(f"{num} is even.")
elif num < 0:
    if num % 2 != 0:
        print(f"{num} is negative odd.")
    else:
        print(f"{num} is negative.")
else:
    print("The number is zero.")