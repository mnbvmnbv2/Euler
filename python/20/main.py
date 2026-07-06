from math import factorial


def main() -> int:
    return sum(int(a) for a in str(factorial(100)))
