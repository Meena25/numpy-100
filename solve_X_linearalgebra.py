"""
Solve for x with linear algebra:
7x + 5y -3z = 16
3x -5y +2z = -8
5x + 3y -7z = 0
"""
import numpy as np

# AX = B
# X = A^-1 B

A = np.array([[7,5,-3],[3,-5,2],[5,3,-7]])

B = np.array([[16],[-8],[0]])

# x = (inverse of A)B
X = np.dot(np.linalg.inv(A),B)

print("Solution for x:")
print(X)
