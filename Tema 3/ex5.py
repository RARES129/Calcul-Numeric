import numpy as np
from numpy.linalg import inv, norm
from ex2 import (
    column_convertor,
    get_norm,
    householder_transformation,
    qr_step_factorization,
)


def calculate_inverse(q, r):
    """
    Calculate inverse of matrix using QR decomposition
    """
    return np.matmul(inv(r), np.transpose(q))


n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
# A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]], dtype=float)
A = (np.random.rand(n, n) - 0.5) * 20
Q = np.identity(n)
R = A.astype(float)

for i in range(n):
    Q, R = qr_step_factorization(Q, R, i, n)

# Calculate inverse using Householder transformation (QR decomposition)
householder_inverse = calculate_inverse(Q, R)

# Calculate inverse using library function
lib_inverse = inv(A)

# Calculate norm difference between two inverses
norm_difference = norm(householder_inverse - lib_inverse)

print("Householder Inverse: \n", householder_inverse)
print("\nLibrary Inverse: \n", lib_inverse)
print("\nNorm Difference: ", norm_difference)
