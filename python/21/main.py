def sum_of_divisors(n: int) -> int:
    return sum(a for a in range(1, n // 2 + 1) if n % a == 0)


def main() -> int:
    ambicables = set()
    skip = set()
    for i in range(1, 10000):
        if i in ambicables or i in skip:
            continue
        s = sum_of_divisors(i)
        if sum_of_divisors(s) == i and s != i:
            ambicables.add(i)
            ambicables.add(s)
        else:
            skip.add(s)
    return sum(ambicables)
