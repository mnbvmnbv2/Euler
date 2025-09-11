import importlib
import timeit
from pathlib import Path


def main(times: int = 10):
    results = {}
    for path in Path("python").rglob("*.py"):
        if path.name == "__init__.py":
            continue
        module = importlib.import_module(str(path).replace("\\", ".")[:-3])
        
        # benchmark
        tot_time = timeit.timeit(module.main, number=times)
        avg_time = tot_time / times
        ans = module.main()

        results[str(path)] = (ans, avg_time)

    # write results as csv file
    with Path("results.csv").open("w") as f:
        f.write("path,answer,time\n")
        for path, (ans, t) in results.items():
            f.write(f"{path},{ans},{t}\n")


if __name__ == "__main__":
    main()