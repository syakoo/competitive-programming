# 19 min
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ls = lmap(int, input().split())

    dp = [[0]*10**4 for _ in range(n+1)]
    for i in range(n):
        dp[i+1][Ls[i]] += 1
        for j in range(10**4):
            dp[i+1][j] += dp[i][j]
    for i in range(n):
        for j in range(1, 10**4):
            dp[i][j] += dp[i][j-1]

    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            Li, Lj = Ls[i], Ls[j]
            l = abs(Li-Lj)
            r = Li+Lj

            ans += dp[i][r-1] - dp[i][l]

    print(ans)


if __name__ == '__main__':
    main()
