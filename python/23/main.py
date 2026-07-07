def main() -> int:
    sums = [0] * (28124 + 1)

    for i in range(1, 28124 // 2):
        for j in range(i * 2, 28124 + 1, i):
            sums[j] += i

    sum_diff = []

    abundant = []
    for i, s in enumerate(sums):
        d = s - i
        sum_diff.append(d)
        if d > 0:
            abundant.append(i)

    abundant_sums = set()

    for idx, i in enumerate(abundant):
        for j in range(idx, len(abundant)):
            d = i + abundant[j]

            abundant_sums.add(d)

    t = 0
    for i in range(28124):
        if i not in abundant_sums:
            t += i

    return t
