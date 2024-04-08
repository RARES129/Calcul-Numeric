import numpy as np


def manual_norm (x):
    return np.sqrt(sum(x_i ** 2 for x_i in x))


def manual_dot (A, B):
    result = [[sum(a * b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]
    return np.array(result, dtype=np.float64)


def manual_outer (a, b):
    return np.array([[a_i * b_j for b_j in b] for a_i in a], dtype=np.float64)


def manual_eye (N):
    return np.array([[1 if i == j else 0 for j in range(N)] for i in range(N)], dtype=np.float64)


def householder_transformation (A):
    rows, cols = A.shape
    Q = manual_eye(rows)
    R = np.copy(A).astype(np.float64)

    for col in range(cols):
        x = R[col:, col]

        e1 = np.zeros_like(x)
        e1[0] = 1
        alpha = -np.copysign(manual_norm(x), x[0])
        v = x - alpha * e1
        v = v / manual_norm(v)

        H = manual_eye(rows)
        H[col:, col:] -= 2.0 * manual_outer(v, v)

        R = manual_dot(H, R)
        Q = manual_dot(Q, H.T)

    return Q, R
