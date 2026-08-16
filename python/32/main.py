nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def main() -> int:
    pandigital = set()
    for a in range(2000):
        for b in range(a, 2000):
            string = f"{a}{b}{a * b}"
            if len(string) < 8:
                continue
            if len(string) > 9:
                break
            if all(num in string for num in nums):
                pandigital.add(a * b)
                print(a, b, a * b)

    return sum(pandigital)
