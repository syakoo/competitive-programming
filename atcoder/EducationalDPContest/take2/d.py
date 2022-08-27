# 7 min
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, W = map(int, input().split())
    WVs = [lmap(int, input().split()) for _ in range(n)]

    dp = [-float('inf')]*(W+1)
    dp[0] = 0
    for w, v in WVs:
        for i in reversed(range(w, W+1)):
            dp[i] = max(dp[i], dp[i-w]+v)

    print(max(dp))


if __name__ == '__main__':
    main()
