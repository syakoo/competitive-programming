# 12 min
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def is_connected(edges, n, edge) -> bool:
    q = deque([0])
    vs = [0]*n
    vs[0] = 1

    while q:
        v = q.popleft()
        for n_v in edges[v]:
            if (v, n_v) == edge or (n_v, v) == edge:
                continue
            if vs[n_v] == 0:
                q.append(n_v)
                vs[n_v] = 1

    return all(vs)


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    edges = [[] for _ in range(n)]

    for a, b in ABs:
        edges[a - 1].append(b - 1)
        edges[b - 1].append(a - 1)

    ans = 0
    for i in range(m):
        if not is_connected(edges, n, (ABs[i][0] - 1, ABs[i][1] - 1)):
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
