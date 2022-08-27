import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    As = lmap(int, input().split())

    if sum(As) - n // 2 <= x:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
