import numpy as np

A = np.array([[-1, -1, 1], [1, 3, 3], [-1, -1, 5]], dtype=float)
m, n = A.shape

eps = pow(10, -10)

# Inițializăm Q și R
Q = np.eye(m)
R = A.copy()

for j in range(n):
    # Calculăm norma vectorului
    normx = sum(R[i, j]**2 for i in range(j, m))**0.5
    if normx == 0:
        continue

    rho = -1 if abs(R[j, j]) < eps else 1
    u1 = R[j, j] - rho * normx
    u = [0]*m
    u[j:] = [R[i, j] / u1 for i in range(j, m)]
    u[j] = 1
    beta = -rho * u1 / normx

    # Actualizăm R
    for k in range(j, m):
        for l in range(j, n):
            R[k, l] -= beta * u[k] * sum(u[i] * R[i, l] for i in range(j, m))

    # Actualizăm Q
    for k in range(m):
        for l in range(j, m):
            Q[k, l] -= beta * u[l] * sum(u[i] * Q[k, i] for i in range(j, m))

# Transpunem Q
Q = Q.T

# Printăm matricile Q și R
print("Q:")
for row in Q:
    print(row)
print("\nR:")
for row in R:
    print(row)
