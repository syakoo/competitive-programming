# 20 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ps = [int(input()) for _ in range(n)]

    Pis = [0]*n
    for i, p in enumerate(Ps):
        Pis[p-1] = i

    mxcnt = 0
    cnt = 0
    for pi, pj in zip(Pis, Pis[1:]):
        if pi < pj:
            cnt += 1
        else:
            mxcnt = max(mxcnt, cnt)
            cnt = 0

    mxcnt = max(mxcnt, cnt)
    print(n - mxcnt - 1)


if __name__ == '__main__':
    main()
