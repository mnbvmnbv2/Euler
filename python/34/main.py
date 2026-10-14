from math import factorial


def main() -> int:
    curious_numbers = []
    for a in range(3, 50_000):
        s = 0
        for i in str(a):
            s += factorial(int(i))
        if s == a:
            curious_numbers.append(a)
    return sum(curious_numbers)
