import functools


@functools.lru_cache
def ways_to_make(n, coins) -> int:
    if n == 0:
        return 1
    if not coins or n < 0:
        return 0
    coin = coins[0]
    choose = ways_to_make(n - coin, coins)
    no_choose = ways_to_make(n, coins[1:])
    return choose + no_choose


def main() -> int:
    return ways_to_make(200, (200, 100, 50, 20, 10, 5, 2, 1))
