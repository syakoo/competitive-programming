# https://algo-method.com/tasks/335
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


MAX = 10**6


def main():
    n = int(input())
    mss = [lmap(int, input().split()) for _ in range(n)]
    dp = [[MAX for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in reversed(range(n)):
            if (r > 0):
                dp[r][c] = mss[r][c] + dp[r-1][c]

            if (c < n-1):
                dp[r][c] = min(dp[r][c], mss[r][c] + dp[r][c+1])

            if (dp[r][c] == MAX):
                dp[r][c] = mss[r][c]

    print(dp[n-1][0])


if __name__ == '__main__':
    main()
