def main(limit: int = 100) -> int:
    sum_of_squares = sum(n**2 for n in range(1, limit + 1))
    square_of_sum = sum(range(1, limit + 1)) ** 2
    n = square_of_sum - sum_of_squares
    return n