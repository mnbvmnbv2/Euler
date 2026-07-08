def main() -> int:
    a = 1
    b = 1
    n = 2

    limit = 10**999

    while True:
        if n % 2 == 0:
            b = a + b
        else:
            a = a + b
        n += 1
        if a > limit or b > limit:
            break
    return n
