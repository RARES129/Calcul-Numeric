import numpy as np
import ex2 as ex2


def solve_linear_system(Q, R, b):
    """
    Solves the linear system Ax = b using QR decomposition.
    """
    y = np.dot(Q.T, b)
    x = np.linalg.solve(R, y)
    return x


def main():
    n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
    # A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]], dtype=float)
    A = (np.random.rand(n, n) - 0.5) * 20
    # b = np.array([3, -1, 5], dtype=float)
    b = (np.random.rand(n) - 0.5) * 20
    print("Input matrix: \n", A)
    Q = np.identity(n)
    R = A.astype(np.float32)
    for i in range(min(n, n)):
        # For each iteration, H matrix is calculated for (i+1)th row
        Q, R = ex2.qr_step_factorization(Q, R, i, n)
    R = np.around(R, decimals=6)
    R = R[:n, :n]
    Q = np.around(Q, decimals=6)
    print("\n")
    print("Q:")
    print(Q)
    print("\n")
    print("R:")
    print(R)

    # Solve the linear system using QR decomposition
    x_qr = solve_linear_system(Q, R, b)
    print("\n")
    print("Solution using QR decomposition:")
    print(x_qr)

    # Solve the linear system using numpy's built-in solver
    x_np = np.linalg.solve(A, b)
    print("\n")
    print("Solution using numpy's built-in solver:")
    print(x_np)

    # Calculate the norm of the difference between the two solutions
    diff_norm = np.around(ex2.get_norm(x_qr - x_np), decimals=4)
    print("\n")
    print("Norm of the difference between the two solutions:")
    print(diff_norm)


if __name__ == "__main__":
    main()
