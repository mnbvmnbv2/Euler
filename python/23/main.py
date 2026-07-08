def main() -> int:
    sums = [0] * (28124 + 1)
    for i in range(1, 28124 // 2):
        for j in range(i * 2, 28124 + 1, i):
            sums[j] += i

    abundant_sums = [0] * 28125

    abundant = []
    abundant_flag = [0] * 28125

    for i, s in enumerate(sums):
        if s - i > 0:
            abundant_flag[i] = 1
            abundant.append(i)

    for i in range(28124):
        for j in abundant:
            if j > i:
                break
            if abundant_flag[i - j]:
                abundant_sums[i] = 1
                break

    return sum(i for i in range(28124) if abundant_sums[i] == 0)


if __name__ == "__main__":
    main()
