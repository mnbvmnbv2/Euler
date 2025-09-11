import numpy as np


def primes(num: int) -> list:
    """Returns prime factors of `num`"""
    list_of_primes = []
    # only check numbers up to sqrt(num)
    sqrt_num = np.ceil(np.sqrt(num))
    # create a list of all numbers up to `num`
    arr = np.arange(2, sqrt_num)
    # remove all non factors
    arr = np.delete(arr, num % arr != 0).astype(int)
    # remove all multiples
    while len(arr) > 0:
        i = arr[0]
        list_of_primes.append(arr[arr % i == 0][0])
        arr = np.delete(arr, arr % i == 0)
    # return
    return list_of_primes


def main(num: int = 600851475143) -> int:
    """Largest prime factor.

    Args:
        num (int, optional): Number to find largest prime factor of. Defaults to 600851475143.

    Returns:
        int: Largest prime factor of `num`
    """
    return max(primes(num))
