def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]

    dists = [[1 << 60 for _ in range(n)] for _ in range(n)]
    adjss = [[] for _ in range(n)]
    ans = 0
    for a, b, c in ABCs:
        adjss[a-1].append((b-1, c))
        dists[a-1][b-1] = c

    for ki in range(n):
        for si in range(n):
            for ti in range(n):
                if si == ti:
                    continue
                d = min(dists[si][ti], dists[si][ki] + dists[ki][ti])
                dists[si][ti] = d
                if d < 1 << 60:
                    ans += d

    print(ans)


if __name__ == '__main__':
    main()
