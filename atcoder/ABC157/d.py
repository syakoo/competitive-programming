import math
import sys
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, k = map(int, input().split())
    ABs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(m)]
    CDs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(k)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a].append(b)
        adjs[b].append(a)

    blocks = [set() for _ in range(n)]
    for c, d in CDs:
        blocks[c].add(d)
        blocks[d].add(c)

    fams = []
    keys = [-1] * n
    for i in range(n):
        if keys[i] > -1:
            continue
        keys[i] = len(fams)
        fam = set([i])
        q = deque([i])
        while q:
            v = q.popleft()
            for vi in adjs[v]:
                if keys[vi] > -1:
                    continue
                keys[vi] = len(fams)
                fam.add(vi)
                q.append(vi)

        fams.append(fam)

    ans = []
    for i, key in enumerate(keys):
        fam = fams[key]
        ans.append(len(fam) - 1 - len(adjs[i]) - len(fam & blocks[i]))

    print(*ans)


if __name__ == '__main__':
    main()
