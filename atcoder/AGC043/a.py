import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    dp = [[h+w]*w for _ in range(h)]
    if Sss[0][0] == '#':
        dp[0][0] = 1
    else:
        dp[0][0] = 0

    for hi in range(h):
        for wi in range(w):
            if hi + 1 < h:
                if Sss[hi][wi] == '.' and Sss[hi + 1][wi] == '#':
                    dp[hi + 1][wi] = min(dp[hi + 1][wi], dp[hi][wi] + 1)
                else:
                    dp[hi + 1][wi] = min(dp[hi + 1][wi], dp[hi][wi])

            if wi + 1 < w:
                if Sss[hi][wi] == '.' and Sss[hi][wi + 1] == '#':
                    dp[hi][wi + 1] = min(dp[hi][wi + 1], dp[hi][wi] + 1)
                else:
                    dp[hi][wi + 1] = min(dp[hi][wi + 1], dp[hi][wi])

    print(dp[h - 1][w - 1])


if __name__ == '__main__':
    main()
