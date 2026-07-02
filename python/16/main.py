def main(num: int = 1000) -> int:
    big = 2**num

    return sum(int(n) for n in str(big))
