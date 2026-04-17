""" This program takes two matrices as input from the user and performs operations such as addition, subtraction, and multiplication using NumPy. It validates the dimensions of the matrices and raises an exception if the dimensions are mismatched. """

import numpy as np

try:
    # taking input for dimensions of matrix A, then taking input for the elements
    r1 = int(input("Enter rows of Matrix A: "))
    c1 = int(input("Enter columns of Matrix A: "))

    print("Enter elements of Matrix A:")
    A = []
    for i in range(r1):
        row = list(map(int, input().split()))

        # checking if the number of elements in the row is equal to the number of columns
        if len(row) != c1:
            raise ValueError("Invalid number of elements in a row of Matrix A")
        A.append(row)
    A = np.array(A)

    # taking input for dimensions of matrix B, then taking input for the elements
    r2 = int(input("\nEnter rows of Matrix B: "))
    c2 = int(input("Enter columns of Matrix B: "))

    print("Enter elements of Matrix B:")
    B = []
    for i in range(r2):
        row = list(map(int, input().split()))

        # checking if the number of elements in the row is equal to the number of columns
        if len(row) != c2:
            raise ValueError("Invalid number of elements in a row of Matrix B")
        B.append(row)
    B = np.array(B)

    # performing matrix addition and subtraction
    try:
        if A.shape != B.shape:
            raise ValueError("Addition/Subtraction not possible due to dimension mismatch.")
        print("\nAddition:\n", A + B)
        print("\nSubtraction:\n", A - B)
    except ValueError as e:
        print("Error:", e)

    # performing matrix multiplication
    try:
        # checking if the number of columns of A is equal to the number of rows of B
        if A.shape[1] != B.shape[0]:
            raise ValueError("Multiplication of these two matrices is not possible.\n Number of column of A must be equal to number of rows of B.")
        print("\nMultiplication:\n", np.dot(A, B))
    except ValueError as e:
        print("Error:", e)
        
# handling other possible errors
except Exception as e:
    print("Error:", e)