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
        v = heapq.heappop(hq)[1]
        if seen[v]:
            continue
        seen[v] = True
        for to, cost in adj[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heapq.heappush(hq, (dist[to], to))

    return dist


if __name__ == '__main__':
    adj = [[(1, 5), (2, 6)], [(2, 10)], [(0, 4)]]

    min_dists = dijkstra(0, len(adj), adj)
    print(min_dists)  # [0, 5, 6]

    min_dists = dijkstra(1, len(adj), adj)
    print(min_dists)  # [14, 0, 10]

    min_dists = dijkstra(2, len(adj), adj)
    print(min_dists)  # [4, 9, 0]
