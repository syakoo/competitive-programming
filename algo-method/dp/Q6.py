# https://algo-method.com/tasks/334
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    mss = [lmap(int, input().split()) for _ in range(n)]
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            dp[r][c] = mss[r][c]

            if (r > 0):
                dp[r][c] = mss[r][c] + dp[r-1][c]

            if (c > 0):
                dp[r][c] = max(dp[r][c], mss[r][c] + dp[r][c-1])

    print(dp[n-1][n-1])


if __name__ == '__main__':
    main()
