'''6. Write a program to display all prime numbers within a user-defined range. 
Additionally, print the count of prime numbers in that range along with their sum. '''

print("\n-----Prime numbers within a range, along with the count and sum of those prime numbers.-----")

# Taking input for the range
start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

# Function to check if a number is prime
def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Finding prime numbers in the given range
prime_numbers = []
for num in range(start, end + 1):
    if check_prime(num):
        prime_numbers.append(num)

# Displaying the results
print(f"\nPrime numbers between {start} and {end}: {prime_numbers}")
print(f"Count of prime numbers: {len(prime_numbers)}")
print(f"Sum of prime numbers: {sum(prime_numbers)}")
