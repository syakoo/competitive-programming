import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, q = map(int, input().split())
    LRs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(m)]
    PQs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(q)]

    trains = [[0]*(n + 1) for _ in range(n)]
    for l, r in LRs:
        trains[l][r] += 1

    for l in range(n-1, -1, -1):
        for r in range(l, n):
            trains[l][r+1] += trains[l][r]
            if l > 0:
                trains[l-1][r] += trains[l][r]
                trains[l-1][r+1] -= trains[l][r]

    for p, q in PQs:
        print(trains[p][q])


if __name__ == '__main__':
    main()
