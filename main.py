import argparse
import importlib
import timeit
from pathlib import Path


def main():
    args = parse_args()
    results = {}
    for path in Path("python").rglob("*.py"):
        if path.name == "__init__.py":
            continue
        module = importlib.import_module(str(path).replace("\\", ".")[:-3])
        
        # benchmark
        benchmark_times = args.benchmark
        if benchmark_times is not None and benchmark_times > 0:
            tot_time = timeit.timeit(module.main, number=benchmark_times)
            avg_time = tot_time / benchmark_times
        else:
            avg_time = -1.0  # indicate no benchmarking was done
        
        ans = module.main()

        results[str(path)] = (ans, avg_time)

    # write results as csv file
    with Path("results.csv").open("w") as f:
        f.write("path,answer,time\n")
        for path, (ans, t) in results.items():
            f.write(f"{path},{ans},{t}\n")

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run all python scripts and optionally benchmark."
    )
    parser.add_argument(
        "-b",
        "--benchmark",
        nargs="?",
        const=10,
        type=int,
        help="Benchmark each module N times (default N=10 if flag is present without a value).",
    )
    return parser.parse_args()

if __name__ == "__main__":
    main()