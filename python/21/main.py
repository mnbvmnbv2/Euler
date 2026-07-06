def main(len: int = 10_000) -> int:
    sums = [0] * (len + 1)

    for i in range(1, len // 2):
        for j in range(i * 2, len + 1, i):
            sums[j] += i
    ambicables = set()
    skip = set()
    for i in range(1, len):
        if i in ambicables or i in skip:
            continue
        s = sums[i]
        if s < len and sums[s] == i and s != i:
            ambicables.add(i)
            ambicables.add(s)
        else:
            skip.add(s)
    return sum(ambicables)
