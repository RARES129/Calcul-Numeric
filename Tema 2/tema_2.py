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
    n = len(A)

    for j in range(n):
        for i in range(j, n):
            sum_l = sum([A[i, k] * A[k, j] for k in range(j)])
            A[i, j] -= sum_l

        for i in range(j + 1, n):
            sum_u = sum([A[j, k] * A[k, i] for k in range(j)])
            A[j, i] = (A[j, i] - sum_u) / A[j, j]
    return A


def matrix_det(A):
    n = len(A)
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det


def solve_system(A, b):
    n = len(A)
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - sum(A[i][j] * y[j] for j in range(i))) / A[i][i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = y[i] - sum(A[i][j] * x[j] for j in range(i + 1, n))

    return x


def euclidean_norm(vector):
    return np.sqrt(np.sum(vector**2))


def on_submit():
    n = int(size_entry.get())
    A = (np.random.rand(n, n) - 0.5) * 20
    A_init = A.copy()
    b = (np.random.rand(n) - 0.5) * 20

    A = crout_factorization(A)
    L = np.tril(A)
    U = np.triu(A)
    for i in range(len(A)):
        U[i][i] = 1
    x_lu = solve_system(A, b)

    euclidean_norma = euclidean_norm(A_init @ x_lu - b)

    result_text.config(state=tk.NORMAL)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"\nA= \n{A_init}\n")
    result_text.insert(tk.END, f"\nL= \n{L}\n")
    result_text.insert(tk.END, f"\nU= \n{U}\n")
    result_text.insert(tk.END, f"\nDeterminantul matricei A este: {matrix_det(A)}\n")
    result_text.insert(tk.END, f"\nSolutia sistemului este: x = {x_lu}\n")
    result_text.insert(tk.END, f"\nNorma euclidiana este: {euclidean_norma}\n")
    if pow(10, -9) > euclidean_norma:
        result_text.insert(
            tk.END, "SOLUTIA ESTE DESTUL DE APROPIATA DE SOLUTIA EXACTA !!!\n"
        )
    result_text.insert(
        tk.END, f"\nSolutia exacta este x=: {np.linalg.solve(A_init, b)}\n"
    )
    result_text.insert(
        tk.END, f"\nInversa matricei A este: \n{np.linalg.inv(A_init)}\n"
    )
    result_text.insert(
        tk.END,
        f"\nSolutia folosind inversa matricei A este x=: {np.linalg.solve(A_init, b)}\n",
    )
    result_text.insert(
        tk.END,
        f"\nNorma euclidiana a diferentei solutiilor este: {euclidean_norm(x_lu - np.linalg.solve(A_init, b))}\n",
    )
    result_text.insert(
        tk.END,
        f"\nNorma euclidiana pentru x_lu - A_inv*b este: {euclidean_norm(x_lu - np.linalg.inv(A_init) @ b)}\n",
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
