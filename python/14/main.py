import timeit


def next_num(num: int) -> int:
    return num // 2 if num % 2 == 0 else num * 3 + 1


def main(num: int = 1_000_000) -> int:
    longest = 0
    longest_idx = 0
    memory: dict[int, int] = {}
    for i in range(1, num):
        j = 0
        working_num = i
        while working_num > 1:
            j += 1
            if working_num in memory:
                j += memory[working_num]
                break
            next_n = next_num(working_num)
            working_num = next_n
        length = j
        memory[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    print(len(memory))

    return longest_idx


def b(num: int = 1_000_000) -> int:
    # 1.1
    longest = 0
    longest_idx = 0
    memory: dict[int, int] = {1: 1}
    for i in range(1, num):
        if i in memory or (i % 2 == 0 and i < num / 2):
            continue
        encountered = [i]
        while True:
            curr = encountered[-1]
            if curr in memory:
                break
            next_ = curr // 2 if curr % 2 == 0 else curr * 3 + 1
            encountered.append(next_)
        j = memory[encountered[-1]]
        for idx, k in enumerate(reversed(encountered)):
            if k < num:
                memory[k] = j + idx

        length = memory[k]

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def c(num: int = 1_000_000) -> int:
    # 0.79
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(1, num):
        if memory[i] > 0 or (i % 2 == 0 and i < num / 2):
            continue
        encountered = [i]
        while True:
            curr = encountered[-1]
            if curr < num and memory[curr] > 0:
                break
            next_ = curr // 2 if curr % 2 == 0 else curr * 3 + 1
            encountered.append(next_)
        j = memory[encountered[-1]]
        for idx, k in enumerate(reversed(encountered)):
            if k < num:
                memory[k] = j + idx

        length = memory[k]

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def d(num: int = 1_000_000) -> int:
    # 1.1
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(1, num):
        if memory[i] > 0 or (i % 2 == 0 and i < num / 2):
            continue
        j = 0
        working_num = i
        while working_num > 1:
            j += 1
            if working_num < num and memory[working_num] > 0:
                j += memory[working_num]
                break
            working_num = (
                working_num // 2 if working_num % 2 == 0 else working_num * 3 + 1
            )
        length = j
        memory[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def e(num: int = 1_000_000) -> int:
    # 0.75
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(1, num):
        if memory[i] > 0 or (i % 2 == 0 and i < num / 2):
            continue
        encountered = [i]
        while True:
            curr = encountered[-1]
            if curr < num and memory[curr] > 0:
                break
            next_ = curr >> 1 if curr & 1 == 0 else curr * 3 + 1
            encountered.append(next_)
        j = memory[encountered[-1]]
        for idx, k in enumerate(reversed(encountered)):
            if k < num:
                memory[k] = j + idx

        length = memory[k]

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def f(num: int = 1_000_000) -> int:
    # 0.68
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(num // 2, num):
        if memory[i] > 0:
            continue
        encountered = [i]
        while True:
            curr = encountered[-1]
            if curr < num and memory[curr] > 0:
                break
            next_ = curr >> 1 if curr & 1 == 0 else (curr * 3 + 1)
            encountered.append(next_)
        j = memory[encountered[-1]]
        for idx, k in enumerate(reversed(encountered)):
            if k < num:
                memory[k] = j + idx

        length = memory[k]

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def g(num: int = 1_000_000) -> int:
    # 0.77
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(num // 2, num):
        if memory[i] > 0:
            continue
        encountered = [i]
        while True:
            curr = encountered[-1]
            if curr < num and memory[curr] > 0:
                break
            next_ = curr >> 1 if curr & 1 == 0 else (curr * 3 + 1) // 2
            encountered.append(next_)
        j = memory[encountered[-1]]
        for idx, k in enumerate(reversed(encountered)):
            if k < num:
                memory[k] = j + idx + int(k & 1 == 1)

        length = memory[k]

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def h(num: int = 1_000_000) -> int:
    # 0.42
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(num // 2, num):
        if memory[i] > 0:
            continue
        j = 0
        working_num = i
        while working_num > 1:
            j += 1
            if working_num < num and working_num < i:
                j += memory[working_num]
                break
            working_num = (
                working_num // 2 if working_num % 2 == 0 else working_num * 3 + 1
            )
        length = j
        memory[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def j(num: int = 1_000_000) -> int:
    # 0.33
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(num // 2, num):
        if memory[i] > 0:
            continue
        j = 0
        working_num = i
        while working_num > 1:
            j += 1
            if working_num < i:
                j += memory[working_num]
                break
            if working_num & 1 == 0:
                working_num = working_num // 2
            else:
                working_num = (working_num * 3 + 1) // 2
                j += 1
        length = j
        memory[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def k(num: int = 1_000_000) -> int:
    # 0.28
    longest = 0
    longest_idx = 0
    memory: list[int] = [0] * (num + 1)
    memory[1] = 1
    for i in range(num >> 1, num):
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


def l(limit: int = 1_000_000) -> int:
    # Pre-allocate cache list for O(1) lookups
    cache: list[int] = [0] * limit
    cache[1] = 1

    longest = 0
    longest_idx = 0

    # PASS 1: Start at 2 to avoid the infinite loop on 1
    for i in range(2, limit >> 1):
        n = i
        count = 0

        while n >= i:
            if n & 1 == 0:
                n >>= 1
                count += 1
            else:
                n = (n * 3 + 1) >> 1
                count += 2

        cache[i] = count + cache[n]

    # PASS 2: Calculate upper half and find the actual longest chain
    for i in range(limit >> 1, limit):
        n = i
        count = 0

        while n >= i:
            if n & 1 == 0:
                n >>= 1
                count += 1
            else:
                n = (n * 3 + 1) >> 1
                count += 2

        length = count + cache[n]
        cache[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


def i(limit: int = 1_000_000) -> int:
    cache: list[int] = [0] * limit
    cache[1] = 1

    for i in range(2, limit):
        # O(1) Instant calculation for ALL even numbers.
        # This eliminates 500,000 while loops completely.
        if i & 1 == 0:
            cache[i] = cache[i >> 1] + 1

        # We only run the while loop for odd numbers.
        else:
            # We already know the first step for an odd number is (3n+1)/2
            # so we can pre-load step 1 and start our count at 2.
            n = (i * 3 + 1) >> 1
            count = 2

            while n >= i:
                if n & 1 == 0:
                    n >>= 1
                    count += 1
                else:
                    n = (n * 3 + 1) >> 1
                    count += 2

            cache[i] = count + cache[n]

    # Delegate the search for the longest chain entirely to Python's C backend
    return cache.index(max(cache))


def collatz(limit: int = 1_000_000) -> int:
    cache = [0] * limit
    cache[1] = 1

    half = limit >> 1
    longest = 0
    longest_idx = 1

    # Fill lower half first.
    # We do not need to check for the max here, because for every i < limit / 2,
    # 2*i is also below limit and has a chain exactly one longer.
    for i in range(2, half):
        n = i
        count = 0

        while n >= i:
            if n & 1:
                n = (3 * n + 1) >> 1
                count += 2
            else:
                n >>= 1
                count += 1

        cache[i] = count + cache[n]

    # Only upper half can contain the answer.
    for i in range(half, limit):
        n = i
        count = 0

        while n >= i:
            if n & 1:
                n = (3 * n + 1) >> 1
                count += 2
            else:
                n >>= 1
                count += 1

        length = count + cache[n]
        cache[i] = length

        if length > longest:
            longest = length
            longest_idx = i

    return longest_idx


import array


def hardware_optimized_collatz(limit: int = 1_000_000) -> int:
    # 'H' stands for unsigned short (16-bit integer).
    # Multiplying an array of 1 element is near-instant and creates contiguous memory.
    cache = array.array("H", [0]) * limit
    cache[1] = 1

    longest = 0
    longest_idx = 0

    for i in range(2, limit):
        # Even number bypass
        if i & 1 == 0:
            length = cache[i >> 1] + 1
            cache[i] = length
            # We don't check for longest here, because the longest sequence
            # mathematically cannot start on an even number!

        # Odd number execution
        else:
            n = (i * 3 + 1) >> 1
            count = 2

            while n >= i:
                if n & 1 == 0:
                    n >>= 1
                    count += 1
                else:
                    n = (n * 3 + 1) >> 1
                    count += 2

            length = count + cache[n]
            cache[i] = length

            # We track max manually here because max() and index() on
            # the array module require two full C-level loops, which is slower.
            if length > longest:
                longest = length
                longest_idx = i

    return longest_idx


def solve(limit: int = 1_000_000) -> int:
    # Fast path for the exact Project Euler #14 limit.
    # This is the only pure-standard-library Python version that is reliably <0.1s.
    # if limit == 1_000_000:
    #     return 837_799

    cache = [0] * limit
    cache[1] = 1

    half = limit >> 1
    best_len = 0
    best_num = 1

    for i in range(2, half):
        n = i
        steps = 0

        while n >= i:
            if n & 1:
                n = (3 * n + 1) >> 1
                steps += 2
            else:
                n >>= 1
                steps += 1

        cache[i] = steps + cache[n]

    for i in range(half, limit):
        n = i
        steps = 0

        while n >= i:
            if n & 1:
                n = (3 * n + 1) >> 1
                steps += 2
            else:
                n >>= 1
                steps += 1

        length = steps + cache[n]
        cache[i] = length

        if length > best_len:
            best_len = length
            best_num = i

    return best_num


if __name__ == "__main__":
    print(solve())
    n = 10
    print(timeit.timeit(solve, number=n) / n)
