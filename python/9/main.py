import math

def main() -> int:
    number = 1000

    for a in range(1, number):
        for b in range(1, number - a):
            c = number - a - b
            if a**2 + b**2 == c**2:
                combinations = (a, b, c)
    a, b, c = combinations
    return a * b * c
