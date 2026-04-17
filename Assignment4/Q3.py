""" This program creates an array of random integers using NumPy, sorts it, and reshapes it into a matrix of valid dimensions. """

import numpy as np

# creating an array of random integers
random_array = np.random.randint(1, 100, 12)
print(f"Random array:\n{random_array}")

# sorting the array
random_array.sort()
print(f"\nSorted array:\n{random_array}")

# reshaping the array into a matrix [3x4]
reshaped_array = random_array.reshape(3, 4)
print(f"\nReshaped Matrix [3x4]:\n{reshaped_array}")