def main() -> int:
    longest = 0
    longest_idx = 0
    for i in range(1000, 1, -1):
        m = 1
        rems = []
        while True:
            _, rem = divmod(m, i)
            m = rem * 10
            if rem in rems:
                x = rems.index(rem)
                leng = len(rems) - x
                break
            rems.append(rem)
        if leng > longest:
            longest_idx = i
            longest = leng
        if i < longest:
            break
    return longest_idx
