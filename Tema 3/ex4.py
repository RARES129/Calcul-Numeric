import numpy as np
from ex2 import (
    get_norm,  # We'll use this for norm calculations
    qr_step_factorization,
    main as ex2_main
)
from ex3 import solve_linear_system


# Assuming ex2_main computes Q, R, and applies sign correction if necessary
# And ex3.solve_linear_system solves the linear system using QR decomposition

# Function to compute vector b, same as in ex1
def compute_vector_b (A, s):
    return np.array([sum(A[i, j] * s[j] for j in range(len(s))) for i in range(len(A))])


# Assuming 'n' is defined or input by the user already
n = int(input("ALEGE MARIMEA MATRICEI PATRATICE: "))
A_init = (np.random.rand(n, n) - 0.5) * 20
s = (np.random.rand(n) - 0.5) * 20

# Calculate vector b using the provided function
b_init = compute_vector_b(A_init, s)

# Call ex2_main to compute Q and R, adjust the function to return them if it doesn't already
Q, R = ex2_main(n)

# Solve the linear system using QR decomposition from ex2 and ex3
x_Householder = solve_linear_system(Q, R, b_init)  # Solution from custom QR decomposition
x_QR = np.linalg.solve(A_init, b_init)  # Solution from numpy's built-in solver

# Compute errors using get_norm from ex2
error1 = get_norm(np.dot(A_init, x_Householder) - b_init)
error2 = get_norm(np.dot(A_init, x_QR) - b_init)
error3 = get_norm(x_Householder - s) / get_norm(s)
error4 = get_norm(x_QR - s) / get_norm(s)

print("\n")
print("||A_init*x_Householder - b_init||2 = ", error1)
print("||A_init*x_QR - b_init||2 = ", error2)
print("||x_Householder - s||2 ||s||2 = ", error3)
print("||x_QR - s||2 / ||s||2 = ", error4)

