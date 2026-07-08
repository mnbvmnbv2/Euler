import math


def main() -> int:

    n = 999_999
    digits = []
    to_pick = list(range(10))

    for i in range(9, -1, -1):
        num_pos = math.factorial(i)
        a, n = divmod(n, num_pos)
        picked = to_pick[a]
        digits.append(picked)
        to_pick.remove(picked)

    return int("".join(map(str, digits)))
