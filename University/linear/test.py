import numpy as np

# Define the two matrices
A = np.array([[1, 2, 9],
              [0, 1, 6],
              [0, 0, 1]])
B = np.array([[1, -2, 3],
              [0, 1, -6],
              [0, 0, 1]])

# Multiply the matrices using numpy.dot

result = np.dot(A, B)

# Print the resulting product matrix
print(result)

