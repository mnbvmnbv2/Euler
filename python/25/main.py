def main() -> int:
    a = 1
    b = 1
    n = 2

    while True:
        if n % 2 == 0:
            b = a + b
        else:
            a = a + b
        n += 1
        if a > (10**999) or b > (10**999):
            break
    return n
