from fractions import Fraction
from math import prod


def main() -> int:
    numerators = []
    denumerators = []
    for a in range(10, 100):
        for b in range(a, 100):
            first_num = int(str(a)[0])
            second_num = int(str(a)[1])
            first_denum = int(str(b)[0])
            second_denom = int(str(b)[1])
            if second_num != first_denum:
                continue
            if first_num == second_num and first_denum == second_denom:
                continue
            if second_denom == 0:
                continue
            if a / b == first_num / second_denom:
                numerators.append(a)
                denumerators.append(b)

    return Fraction(prod(numerators), prod(denumerators)).denominator
