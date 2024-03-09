import numpy as np

eps = pow(10, -10)


def crout_factorization(A):
    n = len(A)

    for j in range(n):
        for i in range(j, n):
            sum_l = sum([A[i, k] * A[k, j] for k in range(j)])
            A[i, j] -= sum_l

        for i in range(j + 1, n):
            sum_u = sum([A[j, k] * A[k, i] for k in range(j)])
            if abs(A[j, j]) < eps:
                raise ValueError(
                    "MATRICEA ESTE SINGULARA SAU NU ARE TOTI DETERMINANTII DE COLT NENULI !!!"
                )
            A[j, i] = (A[j, i] - sum_u) / A[j, j]


def matrix_det(A):
    n = len(A)
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det


def solve_system(L, U, b):
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x


def main():
    A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]])
    A_init = A.copy()
    b = np.array([3, -1, 5])
    crout_factorization(A)
    L = np.tril(A)
    U = np.triu(A)
    for i in range(len(A)):
        U[i][i] = 1
    x = solve_system(L, U, b)
    print(f"L= \n{L}")
    print(f"\nU= \n{U}")
    print("\nSolutia sistemului este: ")
    print(f"x = {x}")


main()
