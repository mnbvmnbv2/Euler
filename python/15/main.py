from math import factorial


def main(num: int = 20) -> int:
    return int(factorial(num * 2) / (factorial(num) * factorial(num)))


if __name__ == "__main__":
    print(main())
