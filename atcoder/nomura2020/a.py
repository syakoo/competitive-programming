import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h1, m1, h2, m2, k = map(int, input().split())
    dh, dm = h2 - h1, m2 - m1
    dt = dh*60 + dm

    print(dt - k)


if __name__ == '__main__':
    main()
