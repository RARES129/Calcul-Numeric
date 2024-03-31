import numpy as np

eps = 1e-10


def manual_copysign (x1, x2):
    return np.abs(x1) if x2 >= 0 else -np.abs(x1)


def norm (x):
    return np.sqrt(np.sum(x ** 2))


def dot_product (x, y):
    return np.sum(x * y)


def householder_transformation (A):
    (rows, cols) = A.shape
    Q = np.identity(rows)

    for r in range(cols):
        x = A[r:, r]

        sigma = dot_product(x, x)
        if sigma == 0:
            continue

        alpha = -manual_copysign(norm(x), x[0])
        u = np.copy(x)
        u[0] -= alpha
        beta = -1. / (alpha * u[0])

        for k in range(r, cols):
            tau = dot_product(u, A[r:, k]) * beta
            A[r:, k] -= tau * u

        for k in range(rows):
            tau = dot_product(u, Q[r:, k]) * beta
            Q[r:, k] -= tau * u

    R = np.copy(A)
    Q = Q.transpose()

    return Q, R


n = int(input("Enter the size of the matrix: "))
A = (np.random.rand(n, n) - 0.5) * 20

Q, R = householder_transformation(A)

print("Matrix A:\n", A)
print("Matrix Q:\n", Q)
print("Matrix R:\n", R)
