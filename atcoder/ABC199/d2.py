
from itertools import combinations
from collections import deque
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def jadge(adjs: list, colors: list, sorted_dims):
    for vi, _ in sorted_dims:
        for vj in adjs[vi]:
            if vj < len(adjs) - 1 and colors[vi] == colors[vj]:
                return False

    return True


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    ans = 0

    adjs = [[] for _ in range(n)]
    dims = [0] * n
    for a, b in ABs:
        adjs[a - 1].append(b - 1)
        adjs[b - 1].append(a - 1)
        dims[a - 1] += 1
        dims[b - 1] += 1

    for v1, v2, v3, v4 in combinations(range(n), 4):
        if v1 in adjs[v2] and v1 in adjs[v3] and v1 in adjs[v4]:
            if v2 in adjs[v3] and v2 in adjs[v4]:
                if v3 in adjs[v4]:
                    print(0)
                    return

    visited = [0] * n
    css = []
    for vi in range(n):
        if visited[vi]:
            continue

        visited[vi] = 1
        cs = [vi]
        q = deque([vi])
        while q:
            vj = q.popleft()
            for vk in adjs[vj]:
                if visited[vk]:
                    continue

                visited[vk] = 1
                q.append(vk)
                cs.append(vk)

        css.append(cs)

    ans = 1
    for c in css:
        if len(c) > 1:
            ans *= 6
        else:
            ans *= 3

    print(ans)


if __name__ == '__main__':
    main()
