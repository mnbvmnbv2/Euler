def main() -> int:
    res = set()
    for a in range(2, 101):
        for b in range(2, 101):
            res.add(a**b)
    return len(res)
