'''4.	Write a program to take a single number as input and display
I. Cube of the number
II. Cube root of the number
III. Natural logarithm of the number 
IV. Base-2 logarithm of the number
V. The number raised to the power of 6
'''

print("\n-----Calculate cube, cube root, natural logarithm, base-2 logarithm, and number raised to power of 6.-----")
# Taking input from the user
num = float(input("Enter a number: "))

# Calculating the cube of the number
cube = num ** 3

# Calculating the cube root of the number
cube_root = num ** (1/3)

# Calculating the natural logarithm of the number
natural_log = 100000000 * (num ** (1/100000000) - 1)

# Calculating the base-2 logarithm of the number
base2_log = 100000000 * (num ** (1/100000000) - 1) / (100000000 * (2 ** (1/100000000) - 1))

# Calculating the number raised to the power of 6
power_of_6 = num ** 6

# Displaying the results
print(f"\nCube of the number: {cube}")
print(f"Cube root of the number: {cube_root}")
print(f"Natural logarithm of the number: {natural_log}")
print(f"Base-2 logarithm of the number: {base2_log}")
print(f"The number raised to the power of 6: {power_of_6}")

