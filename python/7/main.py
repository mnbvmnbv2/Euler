import math

def main(n: int = 10001) -> int:
    primes = []
    to_check = 1
    while len(primes) < n:
        to_check += 1
        is_prime = True
        for i in primes:
            if to_check % i == 0:
                is_prime = False
                break
            if i > math.isqrt(to_check):
                break
        if is_prime:
            primes.append(to_check)
    return primes[-1]