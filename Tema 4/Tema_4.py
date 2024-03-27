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


def gauss_seidel(A, b, max_iterations=1000):
    n = len(b)
    x = [0.0 for _ in range(n)]
    for it_count in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(val * x_new[j] for val, j in A[i] if j < i)
            s2 = sum(val * x[j] for val, j in A[i] if j > i)
            x_new[i] = round(
                (b[i] - s1 - s2) / next(val for val, j in A[i] if j == i), 10
            )
        if all(abs(x_new[i] - x[i]) < eps for i in range(n)):
            break
        x = x_new
    return x, it_count + 1


def main():
    nume_fisier1 = "a_3.txt"
    nume_fisier2 = "b_3.txt"
    data = citire_date_din_fisier(nume_fisier1)
    b = citire_vector_termeni_liberi(nume_fisier2)
    A = memorare_economica(data)
    values, ind_col, inceput_linii = memorare_comprimata(data)
    verificare_diagonala(A, data[0][0])
    solution, iterations = gauss_seidel(A, b)

    # AFISARE PENTERU EXERCITIUL 2
    #--------------------------------
    # for index in range(len(solution)):
    #     print(f"x{index + 1} = {solution[index]}")
    # print("Iterations:", iterations)
    #--------------------------------


if __name__ == "__main__":
    main()
