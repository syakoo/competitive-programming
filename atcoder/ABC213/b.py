import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    sorted_As = sorted(As, reverse=True)
    print(As.index(sorted_As[1]) + 1)


if __name__ == '__main__':
    main()
