''' This program generates a NumPy array of numbers and performs array operations such as 
sum and mean of the array, and largest and smallest values in the array. '''


import numpy as np

# generating a NumPy array
generate = np.arange(10, 70, 10)
print("Generated Array:\n", generate)

# performing array operations
print(f"Sum of elements: {np.sum(generate)}")
print(f"Mean value: {np.mean(generate):.2f}")
print(f"Largest value: {np.max(generate)}")
print(f"Smallest value: {np.min(generate)}")
