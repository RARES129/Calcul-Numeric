epsilon = pow(10, -10)


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


def memorare_economica(data):
    n = data[0][0]
    matrix = [[] for _ in range(n)]
    for value, row, col in data[1:]:
        matrix[row].append((value, col))
    return matrix


def compare_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b):
        return False
    for row_a, row_b in zip(matrix_a, matrix_b):
        dict_a = {col: value for value, col in row_a}
        dict_b = {col: value for value, col in row_b}
        for col in set(dict_a.keys()).union(dict_b.keys()):
            if abs(dict_a.get(col, 0) - dict_b.get(col, 0)) > epsilon:
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


def main():
    data_A = citire_date_din_fisier("a.txt")
    data_B = citire_date_din_fisier("b.txt")
    data_expected_sum = citire_date_din_fisier("aplusb.txt")

    matrix_A = memorare_economica(data_A)
    matrix_B = memorare_economica(data_B)
    expected_summed_matrix = memorare_economica(data_expected_sum)

    computed_summed_matrix = add_matrices(matrix_A, matrix_B)

    if compare_matrices(computed_summed_matrix, expected_summed_matrix):
        print("Suma dintre A si B -> ESTE EGALA cu matricea din fisierul aplusb.txt")
    else:
        print("Suma dintre A si B -> NU ESTE EGALA cu matricea din fisierul aplusb.txt")


if __name__ == "__main__":
    main()
