# https://algo-method.com/tasks/350
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    Ws = lmap(int, input().split())
    MAX = 1 << 60
    # dp[i][wi]: i kome omosa wi no saisyou kosuu
    dp = [[MAX for _ in range(m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(n):
        for wi in range(m+1):
            if dp[i][wi] == -1:
                continue

            dp[i+1][wi] = min(dp[i+1][wi], dp[i][wi])
            if wi + Ws[i] <= m:
                dp[i+1][wi+Ws[i]] = min(dp[i+1][wi+Ws[i]], dp[i][wi] + 1)

    if dp[-1][-1] == MAX:
        print(-1)
        return
    print(dp[-1][-1])


if __name__ == '__main__':
    main()
