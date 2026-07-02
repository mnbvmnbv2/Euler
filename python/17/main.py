translate = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "hundred",
    1000: "onethousand",
}


def get_string_from_num(num: int) -> str:
    if num in translate:
        if num == 100:
            return "one" + translate[100]
        return translate[num]

    if num < 100:
        single = num % 10
        tenner = num // 10 * 10
        return translate[tenner] + translate[single]

    if num < 1000:
        hundreder = num // 100
        remain = num % 100
        if remain == 0:
            return translate[hundreder] + translate[100]
        return (
            translate[hundreder] + translate[100] + "and" + get_string_from_num(remain)
        )


def main(num: int = 1000) -> int:
    nums = []
    for i in range(1, 1001):
        nums.append(get_string_from_num(i))

    return sum(len(n) for n in nums)
