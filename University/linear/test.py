import numpy as np

# Define the two matrices
A = np.array([[0, 1, 1],
              [0, 1, 0],
              [1, 0, 1]])
B = np.array([[-1, 1, 1],
              [0, 1, 0],
              [1, -1, 0]])

# Multiply the matrices using numpy.dot
result = np.dot(A, B)

# Print the resulting product matrix
print(result)

# from numpy.linalg import inv
# a = np.array([[1., 2.], [3., 4.]])
# ainv = inv(a)
