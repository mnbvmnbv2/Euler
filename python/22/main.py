from pathlib import Path


def main() -> int:
    names = Path("python/22/names.txt").read_text().replace('"', "").split(",")
    names.sort()
    total = 0
    for idx, name in enumerate(names):
        name_val = sum((ord(c) - 64) for c in name)
        total += name_val * (idx + 1)

    return total
