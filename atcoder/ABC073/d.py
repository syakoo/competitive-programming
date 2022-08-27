import math
import heapq
from itertools import permutations

INF = math.inf


def dijkstra(s: int, n: int, adj: list) -> list:
    """ダイクストラ法 🐍. O((E+V)log V)

    Args:
        s (int): 始点
        n (int): ノード数
        adj (list): 隣接ノードのリスト。[[(1, 5), (2, 6)], [(2, 10)], [(0, 4)]]

    Returns:
        list: 単一始点最短経路の距離のリスト。
    """
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heapq.heappop(hq)[1]
        if seen[v]:
            continue
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to], to))

    return dist


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, r = map(int, input().split())
    Rs = lmap(lambda x: int(x) - 1, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b, c in ABCs:
        adjs[a-1].append((b-1, c))
        adjs[b-1].append((a-1, c))

    dists = [[math.inf]*n for _ in range(n)]
    for ri in Rs:
        dijks = dijkstra(ri, n, adjs)
        for rj in Rs:
            dists[ri][rj] = dijks[rj]

    ans = math.inf
    for rs in permutations(Rs):
        d = 0
        for i in range(1, len(rs)):
            d += dists[rs[i-1]][rs[i]]

        ans = min(ans, d)

    print(ans)


if __name__ == '__main__':
    main()
