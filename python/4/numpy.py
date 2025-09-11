import numpy as np


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def get_palindromes(num: int) -> list:
    """Get all palindromes up to `num`"""
    arr = np.arange(1, num)
    vfunc = np.vectorize(is_palindrome)
    arr = arr[vfunc(arr)]
    return arr


def main() -> int:
    # get all palindromes up to 999 * 999
    palindromes = get_palindromes(999 * 999)
    # sort in descending order
    palindromes = np.flip(palindromes)
    # get all numbers between 999 and 99
    candidate_factors = np.arange(999, 99, -1)

    for i in palindromes:
        # get mask of all factors of i
        factor_mask = (i % candidate_factors == 0).astype(int)
        # check if there are at least two factors
        if np.count_nonzero(factor_mask) > 1:
            # get all combinations of candidate factors
            factors = candidate_factors[np.where(factor_mask == 1)]
            # check if any pair of candidates produces i
            for j in factors:
                for k in factors:
                    if j * k == i:
                        return i  # , j, k
