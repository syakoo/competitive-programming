# 12 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    s = s.replace("eraser", "_").replace("erase", "_").replace("dreamer", "_").replace(
        "dream", "_").replace("_", "")
    print("YES" if s == "" else "NO")


if __name__ == '__main__':
    main()
