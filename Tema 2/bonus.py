import numpy as np
import tkinter as tk
from tkinter import ttk


eps = pow(10, -10)


def check_valid_matrix(A):
    n = len(A)
    if A.shape[0] != A.shape[1]:
        return False
    for i in range(n):
        if abs(A[i, i]) < eps:
            return False
    if abs(np.linalg.det(A)) < eps:
        return False

    return True


def crout_factorization(A):
    if not check_valid_matrix(A):
        raise ValueError("MATRICEA NU POATE FI DESCOMPUSA !!!")

    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    L_elements = np.zeros(n * (n + 1) // 2)
    U_elements = np.zeros(n * (n + 1) // 2)

    for i in range(n):
        U[i, i] = 1

        for k in range(i, n):
            L[k, i] = A[k, i] - np.dot(L[k, :i], U[:i, i])

        for k in range(i + 1, n):
            U[i, k] = (A[i, k] - np.dot(L[i, :i], U[:i, k])) / L[i, i]

    index = 0
    for i in range(n):
        for j in range(i + 1):
            L_elements[index] = L[i, j]
            index += 1
    index = 0
    for i in range(n):
        for j in range(i, n):
            U_elements[index] = U[i, j]
            index += 1

    return L_elements, U_elements


def solve_LU(L, U, b):
    n = int(np.sqrt(len(L) * 2))

    y = np.zeros(n)
    y[0] = b[0] / L[0]
    for i in range(1, n):
        sum_ly = 0
        for j in range(i):
            sum_ly += L[i * (i + 1) // 2 + j] * y[j]
        y[i] = (b[i] - sum_ly) / L[i * (i + 1) // 2 + i]

    x = np.zeros(n)
    x[n - 1] = y[n - 1] / U[(n - 1) * n // 2 + (n - 1)]
    for i in range(n - 2, -1, -1):
        sum_ux = 0
        for j in range(i + 1, n):
            sum_ux += U[i * n - i * (i + 1) // 2 + j] * x[j]
        x[i] = y[i] - sum_ux

    return x


def euclidean_norm(vector):
    return np.sqrt(np.sum(vector**2))


def on_submit():
    n = int(size_entry.get())
    A = (np.random.rand(n, n) - 0.5) * 20
    b = (np.random.rand(n) - 0.5) * 20

    L, U = crout_factorization(A)
    solution = solve_LU(L, U, b)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "Elementele matricei L:\n")
    result_text.insert(tk.END, f"{L}\n")
    result_text.insert(tk.END, "Elementele matricei U:\n")
    result_text.insert(tk.END, f"{U}\n")
    result_text.insert(tk.END, "\nSoluția sistemului Ax = b este:\n")
    result_text.insert(tk.END, f"{solution}\n")
    result_text.insert(
        tk.END,
        f"\nNorma euclidiană a soluției este: {euclidean_norm(A @ solution - b)}\n",
    )
    if pow(10, -9) > euclidean_norm(A @ solution - b):
        result_text.insert(
            tk.END, "SOLUTIA ESTE DESTUL DE APROPIATA DE SOLUTIA EXACTA !!!\n"
        )
    result_text.config(state=tk.DISABLED)


root = tk.Tk()
root.title("Crout Factorization Solver")

frame = ttk.Frame(root)
frame.grid(row=0, column=0, padx=10, pady=10)

size_label = ttk.Label(frame, text="ALEGE MARIMEA MATRICEI PATRATICE:")
size_label.grid(row=0, column=0, sticky="w")

size_entry = ttk.Entry(frame)
size_entry.grid(row=0, column=1)

submit_button = ttk.Button(frame, text="Submit", command=on_submit)
submit_button.grid(row=0, column=2)

result_text = tk.Text(root, height=20, width=80)
result_text.grid(row=1, column=0, padx=10, pady=10)
result_text.config(state=tk.DISABLED)

root.mainloop()
