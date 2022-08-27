INF = 10**9


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, n = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n)]

    dp = [[INF for _ in range(h + 10**4)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(h + 10**4):
            if j - ABs[i - 1][0] >= 0:
                dp[i][j] = min(dp[i-1][j], dp[i]
                               [j - ABs[i-1][0]] + ABs[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]

    ans = INF
    for j in range(h, h + 10**4):
        ans = min(ans, dp[n][j])

    print(ans)


if __name__ == '__main__':
    main()
