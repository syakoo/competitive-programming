# 7 min 58 sec
from collections import deque
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABCs = [lmap(int, input().split()) for _ in range(n - 1)]
    q, k = map(int, input().split())
    XYs = [lmap(int, input().split()) for _ in range(q)]

    adjs = [[] for _ in range(n)]
    for a, b, c in ABCs:
        adjs[a - 1].append((b - 1, c))
        adjs[b - 1].append((a - 1, c))

    dists = [0]*n
    que = deque([k - 1])
    while que:
        vi = que.popleft()
        for vj, cj in adjs[vi]:
            if dists[vj] > 0:
                continue
            dists[vj] = dists[vi] + cj
            que.append(vj)

    for x, y in XYs:
        print(dists[x - 1] + dists[y - 1])


if __name__ == '__main__':
    main()
