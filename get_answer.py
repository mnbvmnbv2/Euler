import os
import importlib


def get_answer():
    """Get answer for each problem and write to textfile."""
    # get folders
    folders = [name for name in os.listdir(".") if os.path.isdir(name) and not name.startswith(".")]
    for folder in folders:
        module_name = f"{folder}.main"
        module = importlib.import_module(module_name)
        ans = module.main()
        # write answer to textfile
        with open(f"{folder}/answer.txt", "w", encoding="UTF-8") as f:
            f.write(str(ans))


if __name__ == "__main__":
    get_answer()
