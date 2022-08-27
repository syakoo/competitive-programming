import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ts = lmap(int, input().split())

    Tsum = sum(Ts)
    dp = [[False for _ in range(Tsum+1)] for _ in range(n + 1)]
    dp[0][0] = True

    for i in range(n):
        for v in range(Tsum+1):
            if dp[i][v]:
                dp[i+1][v] = True
                dp[i+1][v+Ts[i]] = True

    for v in range(math.ceil(Tsum/2), Tsum+1):
        if dp[-1][v]:
            print(v)
            return

    print(-1)


if __name__ == '__main__':
    main()
