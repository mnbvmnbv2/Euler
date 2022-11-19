def fib(max):
    arr = [1]
    i = 1
    while i < max:
        arr.append(i)
        i = i + arr[-2]
    return arr


def sum_even(arr):
    return sum([i for i in arr if i % 2 == 0])


if __name__ == "__main__":
    print(sum_even(fib(4_000_000)))
