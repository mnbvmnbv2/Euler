inp = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""


def path(nums: list[int], path: list[int]) -> list[int]:
    result = []
    row = 1
    idx = 0
    for move in path:
        result.append(nums[idx])
        # left = + row
        # right = + row + 1
        idx += row + move
        row += 1
    result.append(nums[idx])
    return result


def main() -> int:
    nums = []
    rows = 0
    for row in inp.split("\n"):
        rows += 1
        for num in row.split(" "):
            nums.append(int(num))

    max = 0
    r = []

    for i in range(2 ** (rows - 1)):
        binary = bin(i + 2 ** (rows - 1))
        moves = [int(n) for n in binary[3:]]
        res = path(nums, moves)

        if sum(res) > max:
            max = sum(res)
            r = res

    print(r, sum(r))
    return max


if __name__ == "__main__":
    print(main())
