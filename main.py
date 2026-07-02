import argparse
import csv
import importlib
import timeit
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        description="Run scripts and optionally benchmark."
    )
    parser.add_argument("-b", "--benchmark", nargs="?", const=10, type=int)
    args = parser.parse_args()

    root = Path("python")
    paths = sorted(
        (p for p in root.rglob("*.py") if p.name != "__init__.py"),
        key=lambda p: int(p.relative_to(root).parts[0]),
    )

    rows = []
    for path in paths:
        try:
            module_name = ".".join(path.with_suffix("").parts)
            module = importlib.import_module(module_name)

            n = args.benchmark
            avg = timeit.timeit(module.main, number=n) / n if n and n > 0 else -1.0
            rows.append((path, module.main(), avg))

        except Exception as e:
            print(f"{path}: {e}")

    with Path("results.csv").open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["path", "answer", "time"])
        writer.writerows(rows)


if __name__ == "__main__":
    main()
