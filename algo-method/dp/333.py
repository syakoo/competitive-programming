# https://algo-method.com/tasks/333
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


# dp[r][c] = dp[r-1][c] + dp[r][c-1]
def main():
    n = int(input())
    mss = [list(input()) for _ in range(n)]
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

    dp[1][0] = 1
    for r in range(n):
        for c in range(n):
            if (mss[r][c] == '.'):
                dp[r+1][c+1] = dp[r][c+1] + dp[r+1][c]

    print(dp[n][n])


if __name__ == '__main__':
    main()
