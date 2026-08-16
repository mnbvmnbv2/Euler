ways = []


def ways_to_make(n, coins, having) -> int:
    # print(n, coins, having)
    if n == 0:
        ways.append(having)
        return 1
    if not coins or n < 0:
        return 0
    coin = coins[0]
    choose = ways_to_make(n - coin, coins, having + [coin])
    no_choose = ways_to_make(n, coins[1:], having)
    return choose + no_choose


def main() -> int:
    # ways_to_make(10, [10, 5, 2, 1], [])
    # print(ways)
    return ways_to_make(200, [200, 100, 50, 20, 10, 5, 2, 1], [])
