from itertools import combinations


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a - 1].append(b - 1)
        adjs[b - 1].append(a - 1)

    dp = [[0]*n for _ in range(1 << n)]
    dp[1][0] = 1
    for i in range(2, n+1):
        for vs in combinations(range(n), r=i):
            bit = sum(map(lambda x: 1 << x, vs))

            for vi in vs:
                for vj in adjs[vi]:
                    if bit & (1 << vj):
                        dp[bit][vi] += dp[bit ^ (1 << vi)][vj]

    print(sum(dp[(1 << n) - 1]))


if __name__ == '__main__':
    main()
