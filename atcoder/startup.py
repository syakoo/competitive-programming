import sys
import os


template = """import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    pass


if __name__ == '__main__':
    main()
"""


def main(dir_name: str):
    os.makedirs(f"./{dir_name}", exist_ok=True)
    python_files = ["a.py", "b.py", "c.py", "d.py", "e.py", "f.py"]

    for pyfile in python_files:
        file_name = f"./{dir_name}/{pyfile}"
        if not os.path.isfile(file_name):
            with open(f"./{dir_name}/{pyfile}", mode="w") as f:
                f.write(template)

    with open(f"./{dir_name}/input.txt", mode="w") as f:
        f.write("")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        dir_name = input("ディレクトリ名: ")
    else:
        dir_name = sys.argv[1]

    main(dir_name)
