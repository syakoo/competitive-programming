# https://algo-method.com/tasks/342
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    Ws = lmap(int, input().split())
    Vs = lmap(int, input().split())

    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 0
    for r in range(n):
        for c in range(m + 1):
            if dp[r][c] == -1:
                continue

            dp[r+1][c] = max(dp[r][c], dp[r+1][c])
            if c + Ws[r] <= m:
                dp[r+1][c + Ws[r]] = max(dp[r+1][c + Ws[r]], dp[r][c] + Vs[r])

    print(max(dp[-1]))


if __name__ == '__main__':
    main()
