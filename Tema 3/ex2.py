import numpy as np


def column_convertor (x):
    x.shape = (1, x.shape[0])
    return x


def get_norm (x):
    return np.sqrt(np.sum(np.square(x)))


def householder_transformation (v):
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


def qr_step_factorization (q, r, iter, n):
    v = column_convertor(r[iter:, iter])
    Hbar = householder_transformation(v)
    H = np.identity(n)
    H[iter:, iter:] = Hbar
    r = np.matmul(H, r)
    q = np.matmul(q, H)
    return q, r


def qr_decomposition (A):
    n = A.shape[0]
    Q = np.identity(n)
    R = A.astype(float)
    for i in range(n):
        Q, R = qr_step_factorization(Q, R, i, n)

    # Adjusting signs if necessary
    for i in range(min(Q.shape[0], R.shape[1])):
        if R[i, i] < 0:
            R[i, :] *= -1
            Q[:, i] *= -1

    return Q, R


def main (A):
    #A = (np.random.rand(n, n) - 0.5) * 20
    #print("Input matrix: \n", A)

    Q, R = qr_decomposition(A)

    print("\nQ:")
    print(Q)
    print("\nR:")
    print(R)

    return Q, R  # Return the Q and R matrices


if __name__ == "__main__":
    n = int(input("ALEGE MARIMEA MATRICEI: "))
    A = (np.random.rand(n, n) - 0.5) * 20
    print ("A:\n ", A)
    Q, R = main(A)
