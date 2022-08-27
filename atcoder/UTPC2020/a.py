
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, l = map(int, input().split())
    XAs = [lmap(int, input().split()) for _ in range(n)]
    dp = [0] * n
    dp[0] = XAs[0][1]

    for i in range(1, n):
        dp[i] = max(dp[i - 1] + XAs[i][1] -
                    (XAs[i][0] - XAs[i - 1][0]), XAs[i][1])

    print(max(dp))


if __name__ == '__main__':
    main()
