golden_ratio = 1.61803398875


def fib(n: int) -> int:
    return int(((golden_ratio**n) - (-golden_ratio) ** (-n)) / (5**0.5))


def main():
    even_fib_numbers = []
    i = 1
    while True:
        fib_num = fib(i * 3)
        i += 1
        if fib_num > 4000000:
            break
        even_fib_numbers.append(fib_num)
    return sum(even_fib_numbers)


if __name__ == "__main__":
    main()
