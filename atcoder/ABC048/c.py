# 14 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    As = lmap(int, input().split()) + [0]
    cnt = 0

    for i in range(n):
        diff = (As[i] + As[i + 1]) - x

        if diff > 0:
            ca = min(diff, As[i + 1])
            cnt += diff
            As[i+1] -= ca
            As[i] -= diff - ca

    print(cnt)


if __name__ == '__main__':
    main()
