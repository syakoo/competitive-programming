import math


def main():
    h, w = map(int, input().split())
    S = [list(input()) for _ in range(h)]
    X = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    Y = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    Z = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    dp = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
    dp[1][1] = 1
    mod = 10**9 + 7

    for hi in range(1, h+1):
        for wi in range(1, w+1):
            if S[hi-1][wi-1] == '#' or hi == wi == 1:
                continue
            X[hi][wi] = X[hi][wi-1] + dp[hi][wi-1] % mod
            Y[hi][wi] = Y[hi-1][wi] + dp[hi-1][wi] % mod
            Z[hi][wi] = Z[hi-1][wi-1] + dp[hi-1][wi-1] % mod
            dp[hi][wi] = X[hi][wi] + Y[hi][wi] + Z[hi][wi] % mod

    print(dp[h][w] % mod)


if __name__ == '__main__':
    main()
