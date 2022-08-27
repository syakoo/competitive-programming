import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())
    print('Yes' if a**2 + b**2 < c**2 else 'No')


if __name__ == '__main__':
    main()
