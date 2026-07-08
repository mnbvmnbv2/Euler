import math


def main() -> int:
    n = 999_999
    result = []
    digits = list(range(10))

    for i in range(9, -1, -1):
        num_pos = math.factorial(i)
        a, n = divmod(n, num_pos)
        result.append(digits.pop(a))

    return int("".join(map(str, result)))
