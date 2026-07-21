def main() -> int:
    n = []
    # seems 200k was the last, not sure why
    for i in range(2, 200_000):
        if i == sum(a**5 for a in map(int, str(i))):
            n.append(i)
    return sum(n)
