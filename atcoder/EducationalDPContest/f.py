import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    t = input()
    dp = [['' for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]

    for si, sc in enumerate(s):
        for ti, tc in enumerate(t):
            if sc == tc:
                dp[si + 1][ti + 1] = max(dp[si + 1][ti],
                                         dp[si][ti + 1], dp[si][ti] + sc, key=len)
            else:
                dp[si + 1][ti + 1] = max(dp[si + 1][ti],
                                         dp[si][ti + 1], key=len)

    print(dp[len(s)][len(t)])


if __name__ == '__main__':
    main()
