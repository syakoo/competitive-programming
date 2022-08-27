import math
import heapq

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
        t, v = heapq.heappop(hq)
        if seen[v]:
            continue
        seen[v] = True
        for to, c, d in adj[v]:
            st = max(t, round(d**(1/2))-1)
            res = st+d//(st+1)

            if seen[to] == False and c+res < dist[to]:
                dist[to] = c+res
                heapq.heappush(hq, (dist[to], to))

    return dist


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABCDs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b, c, d in ABCDs:
        adjs[a-1].append((b-1, c, d))
        adjs[b-1].append((a-1, c, d))

    dists = dijkstra(0, n, adjs)
    if dists[-1] >= INF:
        print(-1)
        return
    print(dists[n-1])


if __name__ == '__main__':
    main()
