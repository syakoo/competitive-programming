import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def f(n: int, x: int) -> int:
    if n >= 0:
        return n // x + 1
    else:
        return 0


def main():
    a, b, x = map(int, input().split())
    print(f(b, x) - f(a-1, x))


if __name__ == '__main__':
    main()
