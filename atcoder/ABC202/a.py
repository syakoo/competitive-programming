import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())
    print(7*3 - a - b - c)


if __name__ == '__main__':
    main()
