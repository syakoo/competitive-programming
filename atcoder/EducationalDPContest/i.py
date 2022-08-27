# 20 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ps = lmap(float, input().split())
    m = n // 2
    if n == 1:
        print(Ps[0])
        return

    dp = [[0]*(m + 1) for _ in range(n)]
    dp[0][0] = Ps[0]
    dp[0][1] = 1 - Ps[0]

    for i in range(1, n):
        for mi in range(min(i + 2, m + 1)):
            dp[i][mi] = Ps[i]*dp[i - 1][mi]
            if mi > 0:
                dp[i][mi] += (1 - Ps[i])*dp[i - 1][mi - 1]

    print(sum(dp[n - 1]))


if __name__ == '__main__':
    main()
