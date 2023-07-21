def fib(max):
    arr = [1]
    i = 1
    while i < max:
        arr.append(i)
        i = i + arr[-2]
    return arr


def sum_even(arr):
    return sum([i for i in arr if i % 2 == 0])


def main(length: int = 4_000_000) -> int:
    """Even Fibonacci numbers

    Args:
        length (int, optional): Length of Fibonacci sequence. Defaults to 4_000_000.

    Returns:
        int: Sum of all even Fibonacci numbers up to `length`
    """
    fib_arr = fib(length)
    return sum_even(fib_arr)
