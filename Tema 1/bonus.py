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
    else:
        return 0


def S(i, a):
    sin = T(i, a) / m.sqrt(1 + T(i, a) ** 2)
    return sin


def C(i, a):
    cos = 1 / m.sqrt(1 + T(i, a) ** 2)
    return cos


def bonus(a):
    tan = [
        (4, T(4, a)),
        (5, T(5, a)),
        (6, T(6, a)),
        (7, T(7, a)),
        (8, T(8, a)),
        (9, T(9, a)),
    ]
    for each in tan:
        print(
            f"T({each[0]}, {a}) = {each[1]}, S({each[0]}, {a}) = {S(each[0], a)}, C({each[0]}, {a}) = {C(each[0], a)}"
        )
    print(
        "\n-------------------------------------------------------------------------------------------------------------\n"
    )


def main():
    counter = 1
    while counter < 10000:
        a = random.uniform(-m.pi / 2, m.pi / 2)
        bonus(a)
        counter += 1


main()
