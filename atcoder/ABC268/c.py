import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ps = lmap(int, input().split())

    cnts = [0] * n

    for i in range(n):
        cnts[(Ps[i] - i - 1) % n] += 1
        cnts[(Ps[i] - i) % n] += 1
        cnts[(Ps[i] - i + 1) % n] += 1

    print(max(cnts))


if __name__ == '__main__':
    main()
