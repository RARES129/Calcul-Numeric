import numpy as np
import math as m
import random


def T(i, a):
    if i == 4:
        return (105 * a - pow(a, 3)) / (105 - 45 * pow(a, 2) + pow(a, 4))
    elif i == 5:
        return (945 * a - 105 * pow(a, 3) + pow(a, 5)) / (
            945 - 420 * pow(a, 2) + 15 * pow(a, 4)
        )
    elif i == 6:
        return (10395 * a - 1260 * pow(a, 3) + 21 * pow(a, 5)) / (
            10395 - 4725 * pow(a, 2) + 210 * pow(a, 4) - pow(a, 6)
        )
    elif i == 7:
        return (135135 * a - 17327 * pow(a, 3) + 378 * pow(a, 5) - pow(a, 7)) / (
            135135 - 62370 * pow(a, 2) + 3150 * pow(a, 4) - 28 * pow(a, 6)
        )
    elif i == 8:
        return (
            2027025 * a - 270270 * pow(a, 3) + 6930 * pow(a, 5) - 36 * pow(a, 7)
        ) / (
            2027025
            - 945945 * pow(a, 2)
            + 51975 * pow(a, 4)
            - 630 * pow(a, 6)
            + pow(a, 8)
        )
    elif i == 9:
        return (
            34459425 * a
            - 4729725 * pow(a, 3)
            + 135135 * pow(a, 5)
            - 990 * pow(a, 7)
            + pow(a, 9)
        ) / (
            34459425
            - 16216200 * pow(a, 2)
            + 945945 * pow(a, 4)
            - 13860 * pow(a, 6)
            + 45 * pow(a, 8)
        )


def hierarchy(a, v_exact):

    err1 = abs(T(4, a) - v_exact)
    err2 = abs(T(5, a) - v_exact)
    err3 = abs(T(6, a) - v_exact)
    err4 = abs(T(7, a) - v_exact)
    err5 = abs(T(8, a) - v_exact)
    err6 = abs(T(9, a) - v_exact)

    errors = [(4, err1), (5, err2), (6, err3), (7, err4), (8, err5), (9, err6)]
    sorted_errors = sorted(errors, key=lambda x: x[1])

    print(
        f"T({sorted_errors[0][0]}, {a}), T({sorted_errors[1][0]}, {a}), T({sorted_errors[2][0]}, {a})\n"
    )
    for each in sorted_errors:
        print(f"T({each[0]}, {a}) Error: {each[1]}")

    print("\n-----------------------------------------------------------------------\n")


def main():
    counter = 1
    while counter < 10000:
        a = random.uniform(-m.pi / 2, m.pi / 2)
        v_exact = m.tan(a)
        hierarchy(a, v_exact)
        counter += 1


main()
