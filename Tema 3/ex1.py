import numpy as np

n = 3
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
s = np.array([1, 2, 3])

# Calculăm vectorul b
b = [sum(A[i][j]*s[j] for j in range(n)) for i in range(n)]
print(b)
