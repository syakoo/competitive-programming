from collections import deque
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, k = map(int, input().split())
    Hs = lmap(int, input().split())
    Cs = lmap(lambda x: int(x) - 1, input().split())
    ABs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        if Hs[a] < Hs[b]:
            adjs[a].append(b)
        else:
            adjs[b].append(a)

    dist = [-1]*n
    q = deque()

    for c in Cs:
        q.append(c)
        dist[c] = 0

    while q:
        node = q.popleft()

        for adj_node in adjs[node]:
            if dist[adj_node] == -1:
                dist[adj_node] = dist[node] + 1
                q.append(adj_node)

    print('\n'.join(map(str, dist)))


if __name__ == '__main__':
    main()
