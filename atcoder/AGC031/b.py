from collections import defaultdict


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Cs = [int(input()) for i in range(n)]
    MOD = 10**9 + 7

    stones = [-1, Cs[0]]
    for c in Cs:
        if c != stones[-1]:
            stones.append(c)

    cnts = defaultdict(int)
    n = len(stones)
    dp = [0]*n
    dp[0] = 1
    for i in range(1, n):
        dp[i] = (dp[i - 1] + cnts[stones[i]]) % MOD
        cnts[stones[i]] += dp[i-1]

    print(dp[n-1])


if __name__ == '__main__':
    main()
