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
    n = len(A)

    for j in range(n):
        for i in range(j, n):
            sum_l = sum([A[i, k] * A[k, j] for k in range(j)])
            A[i, j] -= sum_l

        for i in range(j + 1, n):
            sum_u = sum([A[j, k] * A[k, i] for k in range(j)])
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


def euclidean_norm(norm):
    return np.linalg.norm(norm)


def main():
    A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]])
    A_init = A.copy()
    b = np.array([3, -1, 5])

    crout_factorization(A)
    L = np.tril(A)
    U = np.triu(A)
    for i in range(len(A)):
        U[i][i] = 1

    x_lu = solve_system(L, U, b)

    euclidean_norma = euclidean_norm(A_init @ x_lu - b)

    print(f"L= \n{L}")
    print(f"\nU= \n{U}")
    print("\nSolutia sistemului este: ")
    print(f"x = {x_lu}")
    print(f"\nNorma euclidiana este: {euclidean_norma}")
    if pow(10, -9) > euclidean_norma:
        print("Solutia este suficient de apropiata de solutia exacta")
    x_lu = np.linalg.solve(A_init, b)
    print(f"\nSolutia exacta este x=: {x_lu}")
    A_inv = np.linalg.inv(A_init)
    print(f"\nInversa matricei A este: \n{A_inv}")
    x_lib = np.linalg.solve(A_inv, b)
    print(f"\nSolutia folosind inversa matricei A este x=: {x_lib}")
    print(
        f"\nNorma euclidiana a diferentei solutiilor este: {euclidean_norm(x_lu - x_lib)}"
    )
    print(
        f"\nNorma euclidiana pentru x_lu - A_inv*b este: {euclidean_norm(x_lu - A_inv @ b)}"
    )


main()
