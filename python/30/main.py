def main() -> int:
    n = []
    # 9**5 * x until x > 9**5 * x, x = 6
    for i in range(2, 9**5 * 6):
        if i == sum(a**5 for a in map(int, str(i))):
            n.append(i)
    return sum(n)
