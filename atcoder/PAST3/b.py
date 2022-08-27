import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, q = map(int, input().split())
    Ss = [lmap(int, input().split()) for _ in range(q)]

    cnts = [0]*m
    cleareds = [[] for _ in range(n)]
    for s in Ss:
        if s[0] == 1:
            _, ni = s
            score = sum(map(lambda x: n - cnts[x], cleareds[ni - 1]))
            print(score)
        else:
            _, ni, mi = s
            cnts[mi - 1] += 1
            cleareds[ni - 1].append(mi - 1)


if __name__ == '__main__':
    main()
