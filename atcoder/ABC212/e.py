def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, k = map(int, input().split())
    UVs = [lmap(int, input().split()) for _ in range(m)]
    MOD = 998244353

    adjs = [[] for _ in range(n)]
    for u, v in UVs:
        adjs[u-1].append(v-1)
        adjs[v-1].append(u-1)

    dp = [[0]*n for _ in range(k+1)]
    dp[0][0] = 1
    for ki in range(k):
        sm = sum(dp[ki]) % MOD
        for vi in range(n):
            dp[ki+1][vi] = sm - dp[ki][vi]
            for vj in adjs[vi]:
                dp[ki+1][vi] -= dp[ki][vj]
            dp[ki+1][vi] %= MOD

    print(dp[k][0])


if __name__ == '__main__':
    main()
