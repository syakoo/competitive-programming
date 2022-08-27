import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, l = map(int, input().split())
    Xs = lmap(int, input().split())
    t1, t2, t3 = map(int, input().split())

    Xmap = [0]*(l + 5)
    for x in Xs:
        Xmap[x] = 1
    dp = [float('inf') for _ in range(l + 5)]
    dp[0] = 0
    for i in range(l):
        if Xmap[i + 1]:
            dp[i + 1] = min(dp[i + 1], dp[i] + t1 + t3)
        else:
            dp[i + 1] = min(dp[i + 1], dp[i] + t1)

        if Xmap[i + 2]:
            dp[i + 2] = min(dp[i + 2], dp[i] + t1 + t2 + t3)
        else:
            dp[i + 2] = min(dp[i + 2], dp[i] + t1 + t2)

        if Xmap[i + 4]:
            dp[i + 4] = min(dp[i + 4], dp[i] + t1 + 3*t2 + t3)
        else:
            dp[i + 4] = min(dp[i + 4], dp[i] + t1 + 3*t2)

    print(min(dp[l], dp[l + 1]-(t1 + t2)//2, dp[l + 2] -
              (t1 + 3*t2)//2, dp[l + 3]-(t1 + 5*t2) // 2))


if __name__ == '__main__':
    main()
