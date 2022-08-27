
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, l = map(int, input().split())
    Ss = [input() for _ in range(n)]
    Ss.sort()

    print(''.join(Ss))


if __name__ == '__main__':
    main()
