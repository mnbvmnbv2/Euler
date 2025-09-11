"""We find all prime factors of every number up to the limit. Then we find the max number any factor has to be used in any of the numbers.
Then we multiply all those factors their respective number of times."""

def main(limit: int = 20) -> int:
    def get_factors(n: int) -> list[int]:
        factors = []

        for i in range(n - 1, 1, -1): # we can be stricter here, but don't care for low numbers
            if n % i == 0:
                factor = n // i
                factors.extend(get_factors(i))
                factors.extend(get_factors(factor))
                break

        return factors or [n]
        
    factorization = {n: get_factors(n) for n in range(1, limit + 1)}

    factors_to_use = {}
    for n, factors in factorization.items():
        _counter = {}
        for f in factors:
            _counter[f] = _counter.get(f, 0) + 1
        
        for f, count in _counter.items():
            factors_to_use[f] = max(factors_to_use.get(f, 0), count)

    n = 1
    for f, count in factors_to_use.items():
        n *= f ** count
    return n