import functools

coins = (200, 100, 50, 20, 10, 5, 2, 1)


@functools.cache
def ways_to_make(n, idx) -> int:
    if n == 0:
        return 1
    if idx >= len(coins) or n < 0:
        return 0
    coin = coins[idx]
    choose = ways_to_make(n - coin, idx)
    no_choose = ways_to_make(n, idx + 1)
    return choose + no_choose


def main() -> int:
    return ways_to_make(200, 0)
