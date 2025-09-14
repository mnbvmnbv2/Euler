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

chunk_size = 10_000 # this seemed to be enough but still added the part to expand in case we were to look further.
primes = get_primes(chunk_size)

def main(limit: int = 500) -> int:

    def get_tri_num(num: int) -> int:
        return int(num*(num+1)/2)

    def get_num_factors(num: int) -> int:
        primes_in_tri = {}
        global primes
        # if we don't have large enough primes we have to expand
        if primes[-1] < int(num**0.5)+1:
            chunk_size *= 2
            primes = get_primes(chunk_size)
        for prime in primes:
            if num % prime == 0:
                for j in range(2,math.ceil(math.sqrt(num))+1):
                    primes_in_tri[prime] = primes_in_tri.get(prime, 0) + 1
                    if num % prime**(j) != 0:
                        break
            if prime > int(num**0.5)+1:
                break
        return math.prod(v + 1 for v in primes_in_tri.values())

    num_factors_cache = {}

    n = 1
    while True:
        n += 1
        if n%2==0: # n even
            first = n//2
            second = n + 1
        else:
            first = n
            second = (n+1)//2

        if first in num_factors_cache:
            first_num_factors = num_factors_cache[first]
        else:
            first_num_factors = get_num_factors(first)
            num_factors_cache[first] = first_num_factors
        if second in num_factors_cache:
            second_num_factors = num_factors_cache[second]
        else:
            second_num_factors = get_num_factors(second)
            num_factors_cache[second] = second_num_factors

        num_factors = first_num_factors * second_num_factors
        if num_factors >= limit:
            return get_tri_num(n)