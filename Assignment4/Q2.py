""" This program takes a list of numbers as input from the user (at least 12 elements). 
Sorts the list and performs slicing operations to extract elements between index ranges such as 3-6, 6-9, 4-10. """

# taking input from user
num_list = []
print("Enter at least 12 numbers:")
while True:
    try:
        num = int(input())
        num_list.append(num)

        # asking user if they want to continue after entering 12 numbers
        if len(num_list) >= 12:
            print(f"You have entered {len(num_list)} numbers. Do you want to continue? (yes/no)")
            choice = input()
            if choice.lower() == "no":
                break
            else:
                continue

    # error handling for invalid input
    except ValueError:
        print("Invalid input! Please enter a number.")

# sorting the list
num_list.sort()
print("Sorted list:", num_list)

# slicing operations
print("Elements between index 3-6:", num_list[3:6])
print("Elements between index 6-9:", num_list[6:9])
print("Elements between index 4-10:", num_list[4:10])
