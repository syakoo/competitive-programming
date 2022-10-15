import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ss = [input() for _ in range(n)]

    ss.sort(key=lambda x: (int(x), -len(x)))

    print('\n'.join(ss))


if __name__ == '__main__':
    main()
