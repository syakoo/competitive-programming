# https://algo-method.com/tasks/337
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = lmap(int, input().split())
    Ws = lmap(int, input().split())
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = 1

    for ni in range(n):
        for mi in range(m):
            dp[ni+1][mi] += dp[ni][mi]

            if mi + Ws[ni] <= m:
                dp[ni+1][mi + Ws[ni]] += dp[ni][mi]

    print("Yes" if dp[n][m] else "No")


if __name__ == '__main__':
    main()
