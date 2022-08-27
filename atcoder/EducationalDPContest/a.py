def main():
    n = int(input())
    H = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[1] = abs(H[0] - H[1])

    for i in range(2, n):
        dp[i] = min(abs(H[i] - H[i - 2]) + dp[i - 2],
                    abs(H[i] - H[i - 1]) + dp[i - 1])

    print(dp[n - 1])


if __name__ == '__main__':
    main()
