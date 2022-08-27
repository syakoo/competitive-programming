import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, c = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(h)]
    INF = 1 << 60
    dp = [[INF for _ in range(w)] for _ in range(h)]
    ans = INF

    for hi in range(h):
        for wi in range(w):
            if hi > 0:
                dp[hi][wi] = min(dp[hi][wi],
                                 dp[hi-1][wi] + c +
                                 Ass[hi][wi] - Ass[hi-1][wi],
                                 c + Ass[hi][wi] + Ass[hi-1][wi])
            if wi > 0:
                dp[hi][wi] = min(dp[hi][wi],
                                 dp[hi][wi-1] + c +
                                 Ass[hi][wi] - Ass[hi][wi-1],
                                 c + Ass[hi][wi] + Ass[hi][wi-1])

    ans = min(ans, min(min(xs) for xs in dp))
    dp = [[INF for _ in range(w)] for _ in range(h)]

    for hi in range(h-1, -1, -1):
        for wi in range(w):
            if hi < h-1:
                dp[hi][wi] = min(dp[hi][wi],
                                 dp[hi+1][wi] + c +
                                 Ass[hi][wi] - Ass[hi+1][wi],
                                 c + Ass[hi][wi] + Ass[hi+1][wi])
            if wi > 0:
                dp[hi][wi] = min(dp[hi][wi],
                                 dp[hi][wi-1] + c +
                                 Ass[hi][wi] - Ass[hi][wi-1],
                                 c + Ass[hi][wi] + Ass[hi][wi-1])

    ans = min(ans, min(min(xs) for xs in dp))
    print(ans)


if __name__ == '__main__':
    main()
