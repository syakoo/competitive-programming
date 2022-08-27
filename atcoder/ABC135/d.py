import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()

    dp = [[0]*13 for _ in range(len(s) + 1)]
    dp[0][0] = 1
    MOD = 10**9 + 7

    for i, si in enumerate(s[::-1]):
        ex = pow(10, i, 13)
        if si == '?':
            for x in range(13):
                for b in range(10):
                    dp[i+1][x] += dp[i][(x-b*ex) % 13]
                    dp[i+1][x] %= MOD
        else:
            for x in range(13):
                dp[i+1][x] = dp[i][(x-int(si)*ex) % 13] % MOD

    print(dp[len(s)][5])


if __name__ == '__main__':
    main()
