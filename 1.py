def multiples(up_to):
    return sum([i for i in range(up_to) if (i % 5 == 0 or i % 3 == 0)])


if __name__ == "__main__":
    print(multiples(1000))
