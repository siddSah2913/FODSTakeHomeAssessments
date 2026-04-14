'''7.	Write a program to find all numbers between 1000 and 2500 (inclusive) that are divisible by 9 but not by 6. 
Extend the program so that the range limits (1000 and 2500) can also be entered by the user. '''

print("\n-----Numbers between 1000 and 2500 (inclusive) that are divisible by 9 but not by 6.-----\n")

for num in range(1000, 2500 + 1):
    if num % 9 == 0 and num % 6 != 0:
        print(num, end=" ")


print("\n\n-----Numbers between a range-----\n")

# Taking input for the range
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

# Finding numbers divisible by 9 but not by 6
print(f"\nNumbers between {start} and {end} divisible by 9 but not by 6:")

# Displaying the results
for num in range(start, end + 1):
    if num % 9 == 0 and num % 6 != 0:
        print(num, end=" ")
