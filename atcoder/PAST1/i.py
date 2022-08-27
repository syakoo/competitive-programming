from itertools import product
from math import inf


def lmap(func, iter):
    return list(map(func, iter))


def binint(xs: str) -> int:
    result = 0
    for i, x in enumerate(xs):
        if x == 'Y':
            result += 1 << i

    return result


def main():
    n, m = map(int, input().split())
    SCs = [input().split() for _ in range(m)]
    dp = [[inf if i != 0 else 0 for i in range(1 << n)] for _ in range(m + 1)]

    for mi in range(m):
        for ni in range(1 << n):
            dp[mi + 1][ni] = min(dp[mi+1][ni], dp[mi][ni])
            s, c = SCs[mi]
            ni2 = ni | binint(s)
            dp[mi + 1][ni2] = min(dp[mi + 1][ni2], dp[mi][ni] + int(c))

    if dp[m][(1 << n) - 1] < inf:
        print(dp[m][(1 << n) - 1])
    else:
        print(-1)


if __name__ == '__main__':
    main()
