def main_(limit: int = 2_000_000) -> int:
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for i in range(2, int(limit**0.5 + 1)):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False
    return sum(num for num, is_prime in enumerate(primes) if is_prime)