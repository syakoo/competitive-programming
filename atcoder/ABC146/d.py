# 24 min
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n-1)]
    adjs = [[] for _ in range(n)]
    edge_colors = [0] * (n - 1)

    for i, (a, b) in enumerate(ABs):
        adjs[a-1].append((b-1, i))
        adjs[b-1].append((a-1, i))

    q = deque([(0, 0)])
    while q:
        v = q.popleft()

        cur = 0
        for i in range(1, n):
            if i == v[1]:
                continue
            if len(adjs[v[0]]) <= cur:
                break
            if edge_colors[adjs[v[0]][cur][1]] > 0:
                cur += 1
            if len(adjs[v[0]]) <= cur:
                break

            edge_colors[adjs[v[0]][cur][1]] = i
            q.append((adjs[v[0]][cur][0], i))
            cur += 1

    print(max(edge_colors))
    print('\n'.join(lmap(str, edge_colors)))


if __name__ == '__main__':
    main()
