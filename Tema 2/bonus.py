import numpy as np


eps = pow(10, -10)


def check_valid_matrix(A):
    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        return False
    for i in range(n):
        minor = A[: i + 1, : i + 1]
        if abs(np.linalg.det(minor)) < eps:
            return False
    return True


def crout_factorization(A):
    if not check_valid_matrix(A):
        raise ValueError(
            "MATRICEA ESTE SINGULARA SAU NU ARE TOTI DETERMINANTII DE COLT NENULI !!!"
        )

    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    L_elements = np.zeros(n * (n + 1) // 2)
    U_elements = np.zeros(n * (n + 1) // 2)

    for i in range(n):
        U[i, i] = 1

        for k in range(i, n):
            L[k, i] = A[k, i] - np.dot(L[k, :i], U[:i, i])

        for k in range(i + 1, n):
            U[i, k] = (A[i, k] - np.dot(L[i, :i], U[:i, k])) / L[i, i]

    index = 0
    for i in range(n):
        for j in range(i + 1):
            L_elements[index] = L[i, j]
            index += 1
    index = 0
    for i in range(n):
        for j in range(i, n):
            U_elements[index] = U[i, j]
            index += 1

    return L_elements, U_elements


def reconstruct_LU(L_elements, U_elements):
    n = int((-1 + np.sqrt(1 + 8 * len(L_elements))) / 2)
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    index = 0
    for i in range(n):
        for j in range(i + 1):
            L[i, j] = L_elements[index]
            index += 1

    index = 0
    for i in range(n):
        for j in range(i, n):
            U[i, j] = U_elements[index]
            index += 1

    return L, U


def solve_LU(L, U, b):
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)
    return x


def main():

    A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]])
    b = np.array([3, -1, 5])

    L, U = crout_factorization(A)
    print("Elementele matricei L:")
    print(L)
    print("Elementele matricei U:")
    print(U)
    L, U = reconstruct_LU(L, U)
    print("\nMatricea L:")
    print(L)
    print("\nMatricea U:")
    print(U)
    solution = solve_LU(L, U, b)
    print("\nSoluția sistemului Ax = b este:", solution)


main()
