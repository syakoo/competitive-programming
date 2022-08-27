# 10 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [['#' for _ in range(w + 2)] for _ in range(h + 2)]
    MOD = 10**9 + 7

    for hi in range(h):
        s = input()
        for wi in range(w):
            Ass[hi + 1][wi + 1] = s[wi]

    dp = [[0] * (w + 2) for _ in range(h + 2)]
    dp[1][1] = 1
    for hi in range(1, h+1):
        for wi in range(1, w+1):
            if Ass[hi][wi] == '#':
                continue
            dp[hi + 1][wi] += dp[hi][wi]
            dp[hi][wi + 1] += dp[hi][wi]

    print(dp[h][w] % MOD)


if __name__ == '__main__':
    main()
