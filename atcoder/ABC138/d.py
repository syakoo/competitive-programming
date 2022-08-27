
import math
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, q = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n - 1)]
    PXs = [lmap(int, input().split()) for _ in range(q)]
    adjs = [[] for _ in range(n)]
    pnts = [0] * n

    for a, b in ABs:
        adjs[a - 1].append(b - 1)
        adjs[b - 1].append(a - 1)

    for p, x in PXs:
        pnts[p - 1] += x

    visited = [0]*n
    visited[0] = 1
    q = deque([(0, 0)])
    ans = [0]*n

    while q:
        v, p = q.popleft()
        p += pnts[v]
        ans[v] = p

        for adj in adjs[v]:
            if not visited[adj]:
                visited[adj] = 1
                q.append((adj, p))

    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
