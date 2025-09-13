import math

def main_(limit: int = 2_000_000) -> int:
    sum_ = 0
    primes = [2]
    for n in range(3, limit, 2):
        is_prime = True
        for prime in primes:
            if n % prime == 0:
                is_prime = False
                break
            if prime > math.isqrt(n):
                break
        if is_prime:
            sum_ += n
            primes.append(n)
    return sum_