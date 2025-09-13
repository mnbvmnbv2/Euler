import math

def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]

def main(l:int = 999) -> int:
    for n in range(l*2, 1, -1):
        a = math.ceil(n/2)
        b = math.floor(n/2)
        num = a * b
        if is_palindrome(num):
            return num
        for j in range(a, l):
            a += 1
            b -= 1
            num = a * b
            if is_palindrome(num):
                return num
    return 0