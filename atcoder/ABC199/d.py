
import math
import sys
from collections import deque

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    cs = []
    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a - 1].append(b - 1)
        adjs[b - 1].append(a - 1)

    visited = [0] * n
    for vi in range(n):
        if visited[vi]:
            continue

        visited[vi] = 1
        cs.append(vi)
        q = deque([vi])
        while q:
            vj = q.popleft()
            for vk in adjs[vj]:
                if visited[vk]:
                    continue

                visited[vk] = 1
                q.append(vk)

    ans = 1
    for c in cs:
        colors = [-1]*n
        colors[c] = 0
        q = deque([c])
        while q:
            vi = q.popleft()
            for vj in adjs[vi]:
                if colors[vj] == -1:
                    pass


if __name__ == '__main__':
    main()
