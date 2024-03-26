import numpy as np
from numpy.linalg import inv, norm

from ex2 import (
    main as ex2_main
)


def calculate_inverse (q, r):
    return np.matmul(inv(r), np.transpose(q))


n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
# A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]], dtype=float)
A = (np.random.rand(n, n) - 0.5) * 20
Q, R = ex2_main(n)

householder_inverse = calculate_inverse(Q, R)

lib_inverse = inv(A)

norm_difference = norm(householder_inverse - lib_inverse)

print("Householder Inverse: \n", householder_inverse)
print("\nLibrary Inverse: \n", lib_inverse)
print("\nNorm Difference: ", norm_difference)
