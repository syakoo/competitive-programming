
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = set(int(input()) for _ in range(m))
    MOD = 10**9 + 7

    dp = [0]*(n+3)
    dp[0] = 1

    for i in range(n):
        for k in range(1, 3):
            v = i + k
            if v not in As:
                dp[v] += dp[i]
                dp[v] %= MOD

    print(dp[n])


if __name__ == '__main__':
    main()
