import numpy as np

def main(limit: int = 2_000_000) -> int:
    primes = np.ones(limit, dtype=bool)
    primes[0] = False
    primes[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            primes[i*i::i] = False
    return np.sum(np.where(primes)[0])