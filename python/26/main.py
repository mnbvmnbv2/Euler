from decimal import Decimal, getcontext


def main() -> int:
    prec = 10000
    getcontext().prec = prec
    longest = 0
    for i in range(1, 1000):
        frac = Decimal(1) / Decimal(i)
        frac_str = str(frac)
        if len(frac_str) < prec // 2:
            continue
        # why do I have to -3? I thought only the last was imprecice?
        series = str(frac)[-10:1:-10]
        rep = []
        for j in range(prec // 3, 0, -1):
            # print(j, series[:j], series[j : 2 * j])
            if series[:j] == series[j : 2 * j]:
                rep.append(j)
        # we cannot take rep[-1] because it can be polluted by a fake pair in a larger sequence

        if not rep:
            print("failed on", i)
        if len(rep) < 2:
            cycle_l = rep[0]
            print("sus on", i, cycle_l)
            continue
        if len(rep) > 2:
            cycle_l = rep[0] - rep[1]
        if cycle_l > 200:
            print(i, rep, cycle_l)
        longest = max(longest, cycle_l)
    print(longest)
    return longest


if __name__ == "__main__":
    print(main())
