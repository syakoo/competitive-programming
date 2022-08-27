from itertools import product
from collections import deque


def main():
    n, m = map(int, input().split())
    ABs = [list(map(int, input().split())) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a-1].append(b-1)
        adjs[b-1].append(a-1)

    ans = 0
    for colors in product([0, 1], repeat=n):
        colors = list(colors)
        cnt = 1

        if any(colors[a-1] == colors[b-1] == 1 for a, b in ABs):
            continue

        for vs in range(n):
            if colors[vs]:
                continue

            colors[vs] = 2
            q = deque([(vs, 2)])
            while q:
                vi, c = q.popleft()
                nc = (c + 1) % 2 + 2
                for vj in adjs[vi]:
                    if colors[vj] == c:
                        cnt = 0
                        break
                    elif not colors[vj]:
                        colors[vj] = nc
                        q.append((vj, nc))

            if cnt == 0:
                break
            cnt *= 2

        ans += cnt

    print(ans)


main()
