def main(num: int = 1_000_000) -> int:
    longest = 0
    longest_idx = 0
    memory = [0] * (num + 1)
    memory[1] = 1
    for i in range(2, num):
        j = 0
        working_num = i
        while working_num >= i:
            j += 1
            if working_num & 1 == 0:
                working_num = working_num >> 1
            else:
                working_num = (working_num * 3 + 1) >> 1
                j += 1
        j += memory[working_num]
        length = j
        memory[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx
