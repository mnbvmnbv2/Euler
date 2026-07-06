from pathlib import Path


def main() -> int:
    names = sorted(Path("python/22/names.txt").read_text().replace('"', "").split(","))

    return sum(sum((ord(c) - 64) for c in n) * (i + 1) for i, n in enumerate(names))
