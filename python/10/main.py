import math

def main(limit: int = 2_000_000) -> int:
    sum_ = 0
    primes = []
    n = 1
    while True:
        n += 1
        if n > limit:
            break
        is_prime = True
        for i in primes:
            if n % i == 0:
                is_prime = False
                break
            if i > math.isqrt(n):
                break
        if is_prime:
            sum_ += n
            primes.append(n)
    return sum_