import heapq
import math
import sys

sys.setrecursionlimit(10**9)


INF = math.inf


def dijkstra(s: int, n: int, adj: list, k: int) -> list:
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
        if seen[v] or (s != v and v > k):
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
    n, m = map(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]

    adjss = [[] for _ in range(n)]
    for a, b, c in ABCs:
        adjss[a-1].append((b-1, c))

    ans = 0
    for ki in range(n):
        for si in range(n):
            dists = dijkstra(si, n, adjss, ki)
            ans += sum(0 if d >= INF else d for d in dists)

    print(ans)


if __name__ == '__main__':
    main()
