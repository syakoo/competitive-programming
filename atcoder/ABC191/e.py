from heapq import heappush, heappop

INF = 10 ** 9


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]

    for a, b, c in ABCs:
        adj[a - 1].append((b - 1, c))
        adj_r[b - 1].append((a - 1, c))

    dijkstras = []
    for i in range(n):
        dijk = dijkstra(i, n, adj)
        dijkstras.append(dijk)

    for i in range(n):
        ans = INF
        for j, c in adj_r[i]:
            ans = min(ans, dijkstras[i][j] + c)

        if ans >= INF:
            print(-1)
        else:
            print(ans)


def dijkstra(s, n, maps):
    dist = [INF] * n
    hq = [(0, s)]
    dist[s] = 0
    seen = [False] * n
    while hq:
        v = heappop(hq)[1]
        if seen[v]:
            continue
        seen[v] = True
        for to, cost in maps[v]:
            if seen[to] == False and dist[v] + cost < dist[to]:
                dist[to] = dist[v] + cost
                heappush(hq, (dist[to], to))
    return dist


if __name__ == '__main__':
    main()
