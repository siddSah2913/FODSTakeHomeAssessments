""" Write a program to create a function that accepts one string as input and checks whether it is Armstrong or not. Display the output neatly. """

def is_armstrong(num_str):
    armstrong = 0
    for i in num_str:
        armstrong += int(i) ** len(num_str)
    
    return armstrong == int(num_str)

# Taking input from the user
num_str = input("Enter a number: ")

#Calling the function to check if the number is an Armstrong
if is_armstrong(num_str):
    print(f"\n{num_str} is an Armstrong number.")
else:
    print(f"\n{num_str} is not an Armstrong number.")
