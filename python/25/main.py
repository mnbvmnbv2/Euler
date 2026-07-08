def main() -> int:
    a = 1
    b = 1
    n = 2

    limit = 10**999

    while b < limit:
        a, b = b, a + b
        n += 1
    return n
