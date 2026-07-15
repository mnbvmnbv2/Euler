def main() -> int:
    longest = 0
    longest_idx = 0
    for i in range(1, 1000):
        m = 1
        n = i
        j = 0
        seri = []
        rems = []
        while True:
            j += 1
            whole, rem = divmod(m, n)
            # print(f"{m}/{n}", whole, rem)
            m = rem * 10
            seri.append(whole)
            # n = rem
            # or repeat
            if rem in rems:
                x = rems.index(rem)
                leng = len(rems) - x
                # print(leng, x, rem)
                break
            rems.append(rem)
        if leng > longest:
            longest_idx = i
            longest = leng
    return longest_idx
