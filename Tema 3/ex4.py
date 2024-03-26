import numpy as np

from ex2 import (
    get_norm,
    main as ex2_main
)
from ex3 import solve_linear_system


def compute_vector_b (A, s):
    return np.array([sum(A[i, j] * s[j] for j in range(len(s))) for i in range(len(A))])


n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
A_init = (np.random.rand(n, n) - 0.5) * 20
s = (np.random.rand(n) - 0.5) * 20

b_init = compute_vector_b(A_init, s)

Q, R = ex2_main(A_init)

x_Householder = solve_linear_system(Q, R, b_init)
x_QR = np.linalg.solve(A_init, b_init)

error1 = get_norm(np.dot(A_init, x_Householder) - b_init)
error2 = get_norm(np.dot(A_init, x_QR) - b_init)
error3 = get_norm(x_Householder - s) / get_norm(s)
error4 = get_norm(x_QR - s) / get_norm(s)

print("\n")
print("||A_init*x_Householder - b_init||2 = ", error1)
print("||A_init*x_QR - b_init||2 = ", error2)
print("||x_Householder - s||2 / ||s||2 = ", error3)
print("||x_QR - s||2 / ||s||2 = ", error4)
