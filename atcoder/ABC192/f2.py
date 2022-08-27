import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    As = lmap(int, input().split())
    ans = math.inf

    for c in range(1, n+1):
        dp = [[[-math.inf for _ in range(c)]
               for _ in range(n+1)] for _ in range(n+1)]

        for ni in range(n+1):
            dp[ni][0][0] = 0

        for ni in range(1, n+1):
            for ki in range(1, min(ni+1, c+1)):
                for ji in range(c):
                    dp[ni][ki][ji] = max(dp[ni-1][ki][ji],
                                         dp[ni-1][ki-1][(ji - As[ni-1]) % c] + As[ni-1])

        ans_a_sum = dp[n][c][x % c]
        ans = min(ans, (x - ans_a_sum)//c)

    print(ans)


if __name__ == '__main__':
    main()
