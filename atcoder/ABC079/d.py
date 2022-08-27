
import math
import heapq


def lmap(func, iter):
    return list(map(func, iter))


def dijkstra(adjs: list):
    result = [-1]*10
    q = [(0, 1)]
    while q:
        v, i = heapq.heappop(q)
        if result[i] != -1:
            continue

        result[i] = v
        for vij, j in adjs[i]:
            if result[j] == -1:
                heapq.heappush(q, (v+vij, j))

    return result


def main():
    h, w = map(int, input().split())
    Css = [lmap(int, input().split()) for _ in range(10)]
    Ass = [lmap(int, input().split()) for _ in range(h)]

    adjs = [[] for _ in range(10)]
    for ci in range(10):
        for cj in range(10):
            adjs[ci].append((Css[cj][ci], cj))

    min_dists = dijkstra(adjs)
    ans = 0
    for hi in range(h):
        for wi in range(w):
            if Ass[hi][wi] == -1:
                continue

            ans += min_dists[Ass[hi][wi]]

    print(ans)


if __name__ == '__main__':
    main()
