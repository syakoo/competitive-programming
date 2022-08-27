---
to: <%= fileDir %>/_tmp.py
sh: "echo <%= files %> | xargs -n 1 cp <%= fileDir %>/_tmp.py && rm -f <%= fileDir %>/_tmp.py"
---
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))

def main():
    pass


if __name__ == '__main__':
    main()
