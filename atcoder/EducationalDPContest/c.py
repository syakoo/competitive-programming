
def main():
    n = int(input())
    As = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0 for _ in range(3)] for _ in range(n + 1)]

    for ni in range(1, n + 1):
        dp[ni][0] = max(dp[ni - 1][1] + As[ni-1][0],
                        dp[ni - 1][2] + As[ni-1][0])
        dp[ni][1] = max(dp[ni - 1][0] + As[ni-1][1],
                        dp[ni - 1][2] + As[ni-1][1])
        dp[ni][2] = max(dp[ni - 1][1] + As[ni-1][2],
                        dp[ni - 1][0] + As[ni-1][2])

    print(max(dp[n]))


if __name__ == '__main__':
    main()
