def main():
    s = int(input())
    dp = [0] * 3 + [1] * 3 + [0 for _ in range(s)]

    for i in range(6, s+1):
        dp[i] = dp[i-1] + dp[i-3]

    print(dp[s] % (10**9+7))


if __name__ == '__main__':
    main()
