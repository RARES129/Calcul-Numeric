import numpy as np

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


# facut gauss seidel cu a doua memorare
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


def citire():
    numar_fisier = int(input("Introduceti numarul fisierului (1 - 5): "))

    if numar_fisier == 1:
        nume_fisier1 = "a_1.txt"
        nume_fisier2 = "b_1.txt"
    elif numar_fisier == 2:
        nume_fisier1 = "a_2.txt"
        nume_fisier2 = "b_2.txt"
    elif numar_fisier == 3:
        nume_fisier1 = "a_3.txt"
        nume_fisier2 = "b_3.txt"
    elif numar_fisier == 4:
        nume_fisier1 = "a_4.txt"
        nume_fisier2 = "b_4.txt"
    elif numar_fisier == 5:
        nume_fisier1 = "a_5.txt"
        nume_fisier2 = "b_5.txt"
    else:
        print("Numarul introdus nu este valid")
        nume_fisier1, nume_fisier2 = citire()
    return nume_fisier1, nume_fisier2


def main():
    nume_fisier1, nume_fisier2 = citire()
    data = citire_date_din_fisier(nume_fisier1)
    b = citire_vector_termeni_liberi(nume_fisier2)
    A = memorare_economica(data)
    values, ind_col, inceput_linii = memorare_comprimata(data)
    verificare_diagonala(A, data[0][0])
    solution, iterations = gauss_seidel(A, b)
    solution2, iterations2 = gauss_seidel2(values, ind_col, inceput_linii, b)
    print("Prima memorare A:")
    for each in range(0, 5):
        print(A[each])
    print("-----------------------------------------------------")
    print("A doua memorare A:")
    print(f"Valori", values[:5])
    print(f"Indici coloane", ind_col[:5])
    print(f"Inceput linii", inceput_linii[:5])
    print("-----------------------------------------------------")
    print("GAUSS SEIDEL PRIMA MEMORARE:")
    if solution is not None:
        print("Solution:", solution[-10:-1])
        norma = calculate_norm(A, solution, b)
        print("Norma:", norma)
    else:
        print("DIVERGENTA !!!")
    print("Iterations:", iterations)
    print("-----------------------------------------------------")
    print("GAUSS SEIDEL A DOUA MEMORARE:")
    if solution2 is not None:
        print("Solution:", solution2[-10:-1])
        norma = calculate_norm(A, solution2, b)
        print("Norma:", norma)
    else:
        print("DIVERGENTA !!!")
    print("Iterations:", iterations2)


if __name__ == "__main__":
    main()
