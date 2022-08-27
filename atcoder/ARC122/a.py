# 30 min
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    MOD = 10**9 + 7

    dp = [[[0, 0] for _ in range(2)] for _ in range(n)]
    dp[0][0] = [As[0], 1]
    for i in range(n-1):
        dp[i+1][0][1] = (dp[i][0][1] + dp[i][1][1]) % MOD
        dp[i+1][1][1] = dp[i][0][1]
        dp[i+1][0][0] = (dp[i][0][0] + dp[i][1][0] +
                         dp[i+1][0][1]*As[i+1]) % MOD
        dp[i+1][1][0] = (dp[i][0][0] - dp[i+1][1][1]*As[i+1]) % MOD

    print(sum(v for v, _ in dp[-1]) % MOD)


if __name__ == '__main__':
    main()
