import numpy as np
from ex2 import (
    column_convertor,
    get_norm,
    householder_transformation,
    qr_step_factorization,
)


def dot_product(x, y):
    return sum(x_i * y_i for x_i, y_i in zip(x, y))


def euclidean_norm(x):
    return np.sqrt(dot_product(x, x))


A_init = np.array([[1, -1, 1], [1, 3, 3], [-1, -1, 5]], dtype=float)
x_Householder = np.array([1, 1, 1], dtype=float)
x_QR = np.array([1, 1, 1], dtype=float)
b_init = np.array([1, 1, 1], dtype=float)
s = np.array([1, 1, 1], dtype=float)

error1 = euclidean_norm(dot_product(A_init, x_Householder) - b_init)
error2 = euclidean_norm(dot_product(A_init, x_QR) - b_init)
error3 = euclidean_norm(x_Householder - s)
error4 = euclidean_norm(s)
error5 = euclidean_norm(x_QR - s)
error6 = euclidean_norm(s)

print("||A_init*x_Householder - b_init||2 = ", error1)
print("||A_init*x_QR - b_init||2 = ", error2)
print("||x_Householder - s||2 = ", error3)
print("||s||2 = ", error4)
print("||x_QR - s||2 = ", error5)
print("||s||2 = ", error6)
