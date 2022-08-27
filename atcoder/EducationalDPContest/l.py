def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i] = ((-1) ** ((n + 1) % 2)) * As[i]

    for d in range(1, n):
        for l in range(n-d):
            r = l + d
            if (n - (r - l)) % 2 == 0:
                dp[l][r] = min(-As[l] + dp[l+1][r], -As[r] + dp[l][r-1])
            else:
                dp[l][r] = max(As[l] + dp[l+1][r], As[r] + dp[l][r-1])

    print(dp[0][n - 1])


if __name__ == '__main__':
    main()
