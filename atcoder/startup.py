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

this_dir = os.path.dirname(__file__)


def make_files(contest_name: str):
    os.makedirs(f"./{contest_name}", exist_ok=True)
    os.system(f'cd ./{contest_name}')
    python_files = ["a.py", "b.py", "c.py",
                    "d.py", "e.py", "f.py", "g.py", "h.py"]

    for py_file in python_files:
        file_name = f"./{contest_name}/{py_file}"
        if not os.path.isfile(file_name):
            with open(f"./{contest_name}/{py_file}", mode="w") as f:
                f.write(template)

    with open(f"./{contest_name}/input.txt", mode="w") as f:
        f.write("")


def checkout_branch(contest_name: str):
    os.system(f'git checkout -b atcoder/{contest_name}')


def main(contest_name: str):
    os.chdir(this_dir)
    checkout_branch(contest_name)
    make_files(contest_name)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        contest_name = input("コンテスト名: ")
    else:
        contest_name = sys.argv[1]

    main(contest_name)
