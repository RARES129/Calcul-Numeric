import numpy as np

n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
# A = np.array([[1, 1, -1], [2, -1, 1], [1, 3, -2]], dtype=float)
A = (np.random.rand(n, n) - 0.5) * 20
# s = np.array([3, -1, 5], dtype=float)
s = (np.random.rand(n) - 0.5) * 20

# Calculăm vectorul b
b = [sum(A[i][j]*s[j] for j in range(n)) for i in range(n)]
print(b)
