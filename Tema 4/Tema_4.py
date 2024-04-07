import numpy as np
import tkinter as tk

eps = pow(10, -10)


def memorare_economica(data):
    n = data[0][0]
    matrix = [[] for _ in range(n)]
    for value, row, col in data[1:]:
        matrix[row].append((value, col))
    return matrix


def memorare_comprimata(data):
    values = []
    ind_col = []
    inceput_linii = []
    for value, row, col in data[1:]:
        if len(inceput_linii) <= row:
            inceput_linii.append(len(values))
        values.append(value)
        ind_col.append(col)
    inceput_linii.append(len(values))
    return values, ind_col, inceput_linii


def citire_date_din_fisier(nume_fisier):
    data = []
    with open(nume_fisier, "r") as f:
        lines = f.readlines()
        for line in lines:
            elements = line.split(",")
            if len(elements) == 1:
                data.append((int(elements[0].strip()), None, None))
            else:
                value = float(elements[0].strip())
                row = int(elements[1].strip())
                col = int(elements[2].strip())
                data.append((value, row, col))
    return data


def citire_vector_termeni_liberi(fisier):
    with open(fisier, "r") as file:
        n = int(file.readline().strip())
        vector = [float(file.readline().strip()) for _ in range(n)]
    return vector


def verificare_diagonala(matrix, n):
    check = True
    for i in range(n):
        if not any(col == i for _, col in matrix[i]):
            print(f"Elementul de pe diagonala la indexul {i} este zero sau lipsă")
            check = False
    if not check:
        print("MATRICEA NU ARE ELEMENTE EGALE CU 0 SAU LIPSA PE DIAGONALA PRINCIPALA")


def gauss_seidel(A, b, max_iterations=1000):
    n = len(b)
    x = [0.0 for _ in range(n)]
    for it_count in range(max_iterations):
        convergence = True
        for i in range(n):
            old_xi = x[i]
            s1 = sum(val * x[j] for val, j in A[i] if j < i and abs(val) > eps)
            s2 = sum(val * x[j] for val, j in A[i] if j > i and abs(val) > eps)
            x[i] = (b[i] - s1 - s2) / next(val for val, j in A[i] if j == i)
            if abs(x[i] - old_xi) >= eps:
                convergence = False
        if convergence:
            break
        if any(np.isnan(x[i]) or np.isinf(x[i]) for i in range(n)):
            return None, it_count + 1

    return x, it_count + 1


def gauss_seidel2(values, ind_col, inceput_linii, b, max_iter=1000):
    n = len(b)
    x = [0 for _ in range(n)]
    for it_count in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            start = inceput_linii[i]
            end = inceput_linii[i + 1]
            sum1 = sum(
                values[j] * x[ind_col[j]] for j in range(start, end) if ind_col[j] < i
            )
            sum2 = sum(
                values[j] * x_old[ind_col[j]]
                for j in range(start, end)
                if ind_col[j] > i
            )
            diag_index = next(j for j in range(start, end) if ind_col[j] == i)
            x[i] = (b[i] - sum1 - sum2) / values[diag_index]
        if all(abs(x[i] - x_old[i]) < eps for i in range(n)):
            break
        if any(np.isnan(x[i]) or np.isinf(x[i]) for i in range(n)):
            return None, it_count + 1
    return x, it_count + 1


def calculate_norm(A, x_gs, b):
    n = len(b)
    Ax_gs = np.zeros(n)

    for i in range(n):
        Ax_gs[i] = sum(val * x_gs[j] for val, j in A[i])

    norm = np.linalg.norm(Ax_gs - np.array(b), ord=np.inf)
    return norm


def compare_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b):
        return False
    for row_a, row_b in zip(matrix_a, matrix_b):
        dict_a = {col: value for value, col in row_a}
        dict_b = {col: value for value, col in row_b}
        for col in set(dict_a.keys()).union(dict_b.keys()):
            if abs(dict_a.get(col, 0) - dict_b.get(col, 0)) > eps:
                return False
    return True


def add_matrices(matrix_a, matrix_b):
    n = len(matrix_a)
    result = [[] for _ in range(n)]
    for row in range(n):
        dict_a = {col: value for value, col in matrix_a[row]}
        dict_b = {col: value for value, col in matrix_b[row]}
        for col in set(dict_a.keys()).union(dict_b.keys()):
            result[row].append((dict_a.get(col, 0) + dict_b.get(col, 0), col))
    return result


class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gauss Seidel Solver")
        self.geometry("400x300")

        self.file_label = tk.Label(
            self, text="Select input file:", font=("Helvetica", 14)
        )
        self.file_label.pack(pady=10)

        self.file_frame = tk.Frame(self)
        self.file_frame.pack()

        self.file_buttons = []
        for i in range(1, 7):
            if i == 6:
                button = tk.Button(
                    self.file_frame,
                    text=f"Bonus",
                    font=("Helvetica", 12),
                    command=lambda i=i: self.run_solver(i),
                )
            else:
                button = tk.Button(
                    self.file_frame,
                    text=f"File {i}",
                    font=("Helvetica", 12),
                    command=lambda i=i: self.run_solver(i),
                )
            button.pack(side="left", padx=5, pady=5)
            self.file_buttons.append(button)

        self.result_text = tk.Text(self, wrap="word", font=("Helvetica", 12), height=10)
        self.result_text.pack(pady=10, padx=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(self, command=self.result_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_text.config(yscrollcommand=scrollbar.set)

        self.file_paths = [f"a_{i}.txt" for i in range(1, 6)]

    def run_solver(self, index):
        if index == 6:
            matrix_a = memorare_economica(citire_date_din_fisier("a.txt"))
            matrix_b = memorare_economica(citire_date_din_fisier("b.txt"))
            matrix_aplusb = memorare_economica(citire_date_din_fisier("aplusb.txt"))

            result_str = ""
            if compare_matrices(add_matrices(matrix_a, matrix_b), matrix_aplusb):
                result_str += (
                    "Suma dintre A si B -> ESTE EGALA cu matricea din aplusb.txt\n"
                )
            else:
                result_str += (
                    "Suma dintre A si B -> NU ESTE EGALA cu matricea din aplusb.txt\n"
                )

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)
        else:
            nume_fisier1 = self.file_paths[index - 1]
            nume_fisier2 = f"b_{index}.txt"
            data = citire_date_din_fisier(nume_fisier1)
            b = citire_vector_termeni_liberi(nume_fisier2)
            A = memorare_economica(data)
            values, ind_col, inceput_linii = memorare_comprimata(data)
            verificare_diagonala(A, data[0][0])
            solution, iterations = gauss_seidel(A, b)
            solution2, iterations2 = gauss_seidel2(values, ind_col, inceput_linii, b)

            result_str = ""
            if solution is not None:
                result_str += f"GAUSS SEIDEL PRIMA MEMORARE:\nSolution: {solution[-10:-1]}\nNorma: {calculate_norm(A, solution, b)}\nIterations: {iterations}\n\n"
            else:
                result_str += "GAUSS SEIDEL PRIMA MEMORARE:\nDIVERGENTA !!!\n\n"

            if solution2 is not None:
                result_str += f"GAUSS SEIDEL A DOUA MEMORARE:\nSolution: {solution2[-10:-1]}\nNorma: {calculate_norm(A, solution2, b)}\nIterations: {iterations2}"
            else:
                result_str += "GAUSS SEIDEL A DOUA MEMORARE:\nDIVERGENTA !!!"

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, result_str)


if __name__ == "__main__":
    app = Application()
    app.mainloop()
