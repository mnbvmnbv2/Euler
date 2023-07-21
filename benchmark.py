import os
import importlib
import timeit


def benchmark():
    """Run a benchmark on each solution algorithm and write time to file."""
    # get folders
    folders = [name for name in os.listdir(".") if os.path.isdir(name) and not name.startswith(".")]
    for folder in folders:
        module_name = f"{folder}.main"
        module = importlib.import_module(module_name)
        # benchmark
        tot_time = timeit.timeit(module.main, number=1000)
        avg_time = tot_time / 1000
        # write time to file
        with open(f"{folder}/time.txt", "w", encoding="UTF-8") as f:
            f.write(str(avg_time))


if __name__ == "__main__":
    benchmark()
