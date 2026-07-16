def get_primes(limit) -> list[bool]:
    primes = [True] * limit
    primes[0] = False
    primes[1] = False
    for i in range(2, int(limit**0.5 + 1)):
        if primes[i]:
            for j in range(i * i, limit, i):
                primes[j] = False
    return primes


def how_many_primes(a: int, b: int, primes: list[bool]) -> int:
    n = 0
    while True:
        num = n**2 + n * a + b
        if not primes[num]:
            break
        n += 1
    return n


def main() -> int:
    # highest is n = 1000 a = 1000 b = 1000 ish
    # n^2+n*a+b = 2 mil ish
    primes = get_primes(2_100_000)
    primes_up_to_1000 = [idx for idx, p in enumerate(primes[:1000]) if p]
    print(primes_up_to_1000)

    max_n = 0

    ans = 0

    for b in primes_up_to_1000:
        for a in range(-1000, 1000):
            n_primes = how_many_primes(a, b, primes)
            if n_primes > max_n:
                print(n_primes, a, b)
                max_n = n_primes
                ans = a * b
    return ans
