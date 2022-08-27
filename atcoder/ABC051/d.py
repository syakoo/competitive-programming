
import math
import heapq
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def dijk(s: int, n: int, adj: list) -> list:
    dist = [10**8] * n
    hq = [(0, s, -1)]
    dist[s] = 0
    used = [False] * n
    prevs = [-1 for _ in range(n)]

    while hq:
        _, v, prev = heapq.heappop(hq)
        if used[v]:
            continue
        used[v] = True
        prevs[v] = prev
        for to, cost in adj[v]:
            if used[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to], to, v))

    return prevs


def main():
    n, m = map(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b, c in ABCs:
        adjs[a - 1].append((b - 1, c))
        adjs[b - 1].append((a - 1, c))

    edgeset = set()
    for sv in range(n):
        prevs = dijk(sv, n, adjs)
        for vi, prev in enumerate(prevs):
            if prev == -1:
                continue

            edge = list(sorted([vi, prev]))
            edgeset.add(f'{edge[0]}-{edge[1]}')

    print(m - len(edgeset))


if __name__ == '__main__':
    main()
