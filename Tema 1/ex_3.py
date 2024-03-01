import numpy as np
import math as m
import random

def three_mins()


def ex3():
    counter = 1
    min_err1 = 1e9
    min_err2 = 1e9
    min_err3 = 1e9
    min_a1 = 0
    min_a2 = 0
    min_a3 = 0
    while counter < 10000:
        a = random.uniform(-m.pi / 2, m.pi / 2)
        v_exact = m.tan(a)
        error = 1e9

        T4 = (105 * a - pow(a, 3)) / (105 - 45 * pow(a, 2) + pow(a, 4))
        t_error = abs(T4 - v_exact)
        min_erro = min()
        T5 = (945 * a - 105 * pow(a, 3) + pow(a, 5)) / (
            945 - 420 * pow(a, 2) + 15 * pow(a, 4)
        )
        T6 = (10395 * a - 1260 * pow(a, 3) + 21 * pow(a, 5)) / (
            10395 - 4725 * pow(a, 2) + 210 * pow(a, 4) - pow(a, 6)
        )
        T7 = (135135 * a - 17327 * pow(a, 3) + 378 * pow(a, 5) - pow(a, 7)) / (
            135135 - 62370 * pow(a, 2) + 3150 * pow(a, 4) - 28 * pow(a, 6)
        )
        T8 = (2027025 * a - 270270 * pow(a, 3) + 6930 * pow(a, 5) - 36 * pow(a, 7)) / (
            2027025
            - 945945 * pow(a, 2)
            + 51975 * pow(a, 4)
            - 630 * pow(a, 6)
            + pow(a, 8)
        )
        T9 = (
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


def main():
    print(
        "The smallest number that can be added to 1 and still be different from 1 is:"
    )
    ex3()


main()
