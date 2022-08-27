from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, k = map(int, input().split())
    Hs = lmap(int, input().split())
    Cs = lmap(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    adjss = [[] for _ in range(n)]
    for ab in ABs:
        ab.sort(key=lambda x: Hs[x-1])
        adjss[ab[0]-1].append(ab[1]-1)

    dists = [-1]*n
    for c in Cs:
        dists[c-1] = 0
    q = deque(c-1 for c in Cs)
    while q:
        v = q.popleft()

        for vi in adjss[v]:
            if dists[vi] == -1:
                dists[vi] = dists[v] + 1
                q.append(vi)

    print('\n'.join(map(str, dists)))


if __name__ == '__main__':
    main()
