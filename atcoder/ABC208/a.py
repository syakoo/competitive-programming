import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())
    if a <= b <= a*6:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
