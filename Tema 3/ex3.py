import numpy as np

import ex2 as ex2

from ex2 import householder_transformation


def solve_linear_system (Q, R, b):
    y = np.dot(Q.T, b)
    x = np.linalg.solve(R, y)
    return x


def main ():
    n = int(input())
    # A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]], dtype=float)
    A = (np.random.rand(n, n) - 0.5) * 20
    # b = np.array([3, -1, 5], dtype=float)
    b = (np.random.rand(n) - 0.5) * 20
    print("Input matrix: \n", A)
    Q = np.identity(n)
    R = A.astype(np.float32)
    Q,R = householder_transformation(A)
    R = np.around(R, decimals=6)
    R = R[:n, :n]
    Q = np.around(Q, decimals=6)
    print("\n")
    print("Q:")
    print(Q)
    print("\n")
    print("R:")
    print(R)

    x_qr = solve_linear_system(Q, R, b)
    print("\n")
    print("Solution using QR decomposition:")
    print(x_qr)

    x_np = np.linalg.solve(A, b)
    print("\n")
    print("Solution using numpy's built-in solver:")
    print(x_np)

    diff_norm = np.around(ex2.get_norm(x_qr - x_np), decimals=4)
    print("\n")
    print("Norm of the difference between the two solutions:")
    print(diff_norm)


if __name__ == "__main__":
    main()
