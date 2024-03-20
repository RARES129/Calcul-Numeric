import numpy as np


def column_convertor(x):
    """
    Converts 1d array to column vector
    """
    x.shape = (1, x.shape[0])
    return x


def get_norm(x):
    """
    Returns Norm of vector x
    """
    return np.sqrt(np.sum(np.square(x)))


def householder_transformation(v):
    """
    Returns Householder matrix for vector v
    """
    size_of_v = v.shape[1]
    e1 = np.zeros_like(v)
    e1[0, 0] = 1
    vector = get_norm(v) * e1
    if v[0, 0] < 0:
        vector = -vector
    u = (v + vector).astype(np.float32)
    H = np.identity(size_of_v) - (
        (2 * np.matmul(np.transpose(u), u)) / np.matmul(u, np.transpose(u))
    )
    return H


def qr_step_factorization(q, r, iter, n):
    """
    Return Q and R matrices for iter number of iterations.
    """
    v = column_convertor(r[iter:, iter])
    Hbar = householder_transformation(v)
    H = np.identity(n)
    H[iter:, iter:] = Hbar
    r = np.matmul(H, r)
    q = np.matmul(q, H)
    return q, r


def main():
    A = np.array([[1, -1, 1], [1, 3, 3], [-1, -1, 5]], dtype=float)
    n, m = A.shape
    print("Input matrix: \n", A)
    Q = np.identity(n)
    R = A.astype(float)
    for i in range(min(n, m)):
        # For each iteration, H matrix is calculated for (i+1)th row
        Q, R = qr_step_factorization(Q, R, i, n)
    min_dim = min(m, n)
    R = np.around(R, decimals=7)
    R = R[:min_dim, :min_dim]
    Q = np.around(Q, decimals=7)
    print("\n")
    print("Q:")
    print(Q)
    print("\n")
    print("R:")
    print(R)
    


if __name__ == "__main__":
    main()
