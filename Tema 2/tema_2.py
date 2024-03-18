import numpy as np

eps = pow(10, -10)


def check_valid_matrix(A):
    n = len(A)
    if A.shape[0] != A.shape[1]:
        return False
    for i in range(n):
        if abs(A[i, i]) < eps:
            return False
    if abs(np.linalg.det(A)) < eps:
        return False

    return True


def crout_factorization(A):
    if not check_valid_matrix(A):
        raise ValueError("MATRICEA NU POATE FI DESCOMPUSA !!!")
    n = len(A)

    for j in range(n):
        for i in range(j, n):
            sum_l = sum([A[i, k] * A[k, j] for k in range(j)])
            A[i, j] -= sum_l

        for i in range(j + 1, n):
            sum_u = sum([A[j, k] * A[k, i] for k in range(j)])
            A[j, i] = (A[j, i] - sum_u) / A[j, j]
    return A


def matrix_det(A):
    n = len(A)
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det


def solve_system(A, b):
    n = len(A)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(A[i][j] * y[j] for j in range(i))) / A[i][i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))

    return x


def euclidean_norm(vector):
    return np.sqrt(np.sum(vector**2))


def main():
    n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
    A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]], dtype=float)
    # A = (np.random.rand(n, n) - 0.5) * 20

    A_init = A.copy()
    b = np.array([3, -1, 5], dtype=float)
    # b = (np.random.rand(n) - 0.5) * 20

    A = crout_factorization(A)
    L = np.tril(A)
    U = np.triu(A)
    for i in range(len(A)):
        U[i][i] = 1
    x_lu = solve_system(A, b)

    euclidean_norma = euclidean_norm(A_init @ x_lu - b)
    print(
        "--------------------------------------------------------------------------------------------"
    )
    print(f"\nA= \n{A_init}")
    print(
        "--------------------------------------------------------------------------------------------"
    )
    print(f"\nL= \n{L}")
    print(
        "--------------------------------------------------------------------------------------------"
    )
    print(f"\nU= \n{U}")
    print(
        "--------------------------------------------------------------------------------------------"
    )

    print(f"\nDeterminantul matricei A este: {matrix_det(A)}")
    print(
        "--------------------------------------------------------------------------------------------"
    )

    print("\nSolutia sistemului este: ")
    print(f"x = {x_lu}")
    print(
        "--------------------------------------------------------------------------------------------"
    )

    print(f"\nNorma euclidiana este: {euclidean_norma}")
    if pow(10, -9) > euclidean_norma:
        print("SOLUTIA ESTE DESTUL DE APROPIATA DE SOLUTIA EXACTA !!!")
    print(
        "--------------------------------------------------------------------------------------------"
    )

    x_lu = np.linalg.solve(A_init, b)
    print(f"\nSolutia exacta este x=: {x_lu}")
    print(
        "--------------------------------------------------------------------------------------------"
    )
    A_inv = np.linalg.inv(A_init)
    print(f"\nInversa matricei A este: \n{A_inv}")
    print(
        "--------------------------------------------------------------------------------------------"
    )
    x_lib = np.linalg.solve(A_inv, b)
    print(f"\nSolutia folosind inversa matricei A este x=: {x_lib}")
    print(
        "--------------------------------------------------------------------------------------------"
    )
    print(
        f"\nNorma euclidiana a diferentei solutiilor este: {euclidean_norm(x_lu - x_lib)}"
    )
    print(
        "--------------------------------------------------------------------------------------------"
    )
    print(
        f"\nNorma euclidiana pentru x_lu - A_inv*b este: {euclidean_norm(x_lu - A_inv @ b)}"
    )
    print(
        "--------------------------------------------------------------------------------------------"
    )


main()

