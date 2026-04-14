''' 9.	Write a menu-driven program that repeatedly asks the user for numbers and computes the separate sums of positive and negative numbers. 
Continue until the user chooses to exit the program. '''

sum_positive = 0
sum_negative = 0

while True:
    print("\n-----***** Numbers Addition Menu *****-----")
    print("1. Enter a number")
    print("2. Exit")
    
    choice = input("\nEnter your choice: ")
    
    if choice == '1':
        try:
            num = float(input("\nEnter a number: "))
            if num > 0:
                sum_positive += num
            elif num < 0:
                sum_negative += num
            else:
                print("\nZero does not affect the sums.")
        except ValueError:
            print("\nInvalid input! Please enter a valid number.")
            
    elif choice == '2':
        print("\n----- Final Results -----")
        print(f"Sum of positive numbers: {sum_positive}")
        print(f"Sum of negative numbers: {sum_negative}")
        print("\nExiting program.......")
        break
    else:
        print("Invalid choice! Please select 1 or 2.")
