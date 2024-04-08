import numpy as np

from ex2 import householder_transformation

eps = 1e-10


def manual_norm (x):
    return np.sqrt(np.sum(x ** 2))


def manual_dot (A, B):
    result = np.zeros((A.shape[0], B.shape[1]))
    for i in range(A.shape[0]):
        for j in range(B.shape[1]):
            for k in range(A.shape[1]):
                result[i, j] += A[i, k] * B[k, j]
    return result


def upper_triangular_multiply (R, Q):
    return manual_dot(R, Q)


def is_converged (Ak1, Ak, eps):
    difference = manual_norm(Ak1 - Ak)
    return difference < eps


def householder_iterative_process (A, eps):
    Ak = A.copy()
    k = 0
    while True:
        Q, R = householder_transformation(Ak)
        Ak1 = manual_dot(R, Q)

        change_norm = manual_norm(Ak1 - Ak)
        print(f"Iteratia {k}:\n")
        print(f"Ak1:\n{Ak1}\n")
        print(f"Norma actualizata: {change_norm}\n")
        print("-----------------------------------------------------------------------\n")

        if change_norm < eps:
            print("S-A AJUNS LA CONVERGENTA!!!.\n")
            break

        Ak = Ak1
        k += 1
        if k > 100:
            print("Nu s-a ajuns la convergenta in 100 de iteratii.\n")
            break

    return Ak, k


n = int(input())
A = (np.random.rand(n, n) - 0.5) * 20
A = (A + A.T) / 2

print("Matricea initiala:\n", A)
Ak, num_iterations = householder_iterative_process(A, 1e-10)

print(f"Numar iteratii: {num_iterations}\n")
print("Limita aproximativa:\n", Ak)
