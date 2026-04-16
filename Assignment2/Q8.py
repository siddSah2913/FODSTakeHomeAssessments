""" Write a program to accept a list of numbers from the user and return a new list with all duplicates removed and the numbers sorted in ascending order. """

def remove_duplicates(numbers):
    unique_numbers = []
    for num in numbers:
        # If the number is not already in the unique_numbers list, add it
        if num not in unique_numbers:
            unique_numbers.append(num)

    # Sort the unique numbers in ascending order
    unique_numbers.sort()
    return unique_numbers

# Taking input from the user
numbers_input = input("\nEnter a list of numbers separated by commas: ")

# Create an empty list to store the numbers after processing the input
numbers_list = []

# Split the input string by commas
numbers_split = numbers_input.split(",")

# Convert the split strings to integers and remove extra spaces
for num in numbers_split:
    numbers_list.append(int(num.strip()))

# Calling the function
unique_numbers = remove_duplicates(numbers_list)

print("\nList of unique numbers:")
for num in unique_numbers:
    print(num)