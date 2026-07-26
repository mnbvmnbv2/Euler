# ways = []


def ways_to_make(n, coins, having) -> int:
    if not coins:
        return 0
    if n == 0:
        # ways.append(having)
        return 1
    for coin in reversed(coins):
        if coin <= n:
            choose = ways_to_make(n, [c for c in coins if c != coin], having)
            no_choose = ways_to_make(n - coin, coins, having + [coin])
            return choose + no_choose
    return 0


def main(target=200) -> int:
    return ways_to_make(200, [1, 2, 5, 10, 20, 50, 100, 200], [])
