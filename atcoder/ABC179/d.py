def main():
    n, k = map(int, input().split())
    LRs = [list(map(int, input().split())) for _ in range(k)]
    dp = [0, 1] + [0] * n

    for i in range(2, n+1):
        dp[i] = dp[i-1]
        for l, r in LRs:
            dp[i] += dp[max(i-l, 0)] - dp[max(i-r-1, 0)]
            dp[i] %= 998244353

    print((dp[n]-dp[n-1]) % 998244353)


if __name__ == '__main__':
    main()
