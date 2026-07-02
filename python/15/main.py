from math import factorial


def main(num: int = 20) -> int:
    return int(factorial(num * 2) / (factorial(num) * factorial(num)))
