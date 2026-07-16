def main(to_: int = 1001) -> int:
    sum = 1
    n = 1
    for i in range(2, to_, 2):
        for _ in range(4):
            n += i
            sum += n
    return sum
