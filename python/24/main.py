import itertools


def main() -> int:
    for i, p in enumerate(itertools.permutations(range(10), r=10)):
        if i == 999_999:
            return int("".join(str(a) for a in p))
    return 1
