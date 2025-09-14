import math

import numpy as np

def get_primes(limit: int) -> int:
    primes = np.ones(limit, dtype=bool)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            primes[i*i::i] = False
    return [n for n, is_prime in enumerate(primes) if is_prime]

def main_(limit: int = 500) -> int:
    max_tri = 14_000 # hardcoded
    tri_of_max = sum(range(1, max_tri + 1))
    primes = get_primes(int(tri_of_max**0.5)+1)

    def get_tri_num(num: int) -> int:
        return int(num*(num+1)/2)

    def get_num_factors(num: int) -> int:
        primes_in_tri = {}
        for prime in primes:
            if num % prime == 0:
                for j in range(2,math.ceil(math.sqrt(num))+1):
                    primes_in_tri[prime] = primes_in_tri.get(prime, 0) + 1
                    if num % prime**(j) != 0:
                        break
            if prime > int(num**0.5)+1:
                break

        return math.prod(v + 1 for v in primes_in_tri.values())

    get_tri = np.vectorize(get_tri_num)
    get_factors = np.vectorize(get_num_factors)
    tri_nums = get_tri(np.arange(max_tri))
    num_factors = get_factors(tri_nums)
    indices_over_limit = np.where(num_factors > limit)[0]
    return tri_nums[indices_over_limit][0]