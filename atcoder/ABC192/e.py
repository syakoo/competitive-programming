import heapq
import math


def lmap(func, iter):
    return list(map(func, iter))


INF = math.inf


def main():
    n, m, x, y = map(int, input().split())
    ABTKs = [lmap(int, input().split()) for _ in range(m)]
    adj = [[] for _ in range(n)]

    for a, b, t, k in ABTKs:
        adj[a-1].append((b-1, t, k))
        adj[b-1].append((a-1, t, k))

    dist = [INF] * n
    hq = [(0, x-1)]
    dist[x-1] = 0
    seen = [False] * n

    while hq:
        v = heapq.heappop(hq)
        if seen[v[1]]:
            continue
        seen[v[1]] = True
        for to, t, k in adj[v[1]]:
            cost = t + (- v[0] % k)
            if seen[to] == False and dist[v[1]] + cost < dist[to]:
                dist[to] = dist[v[1]] + cost
                heapq.heappush(hq, (dist[to], to))

    if dist[y-1] >= INF:
        print("-1")
    else:
        print(dist[y-1])


if __name__ == '__main__':
    main()
