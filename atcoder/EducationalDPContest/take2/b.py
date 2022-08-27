def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Hs = lmap(int, input().split())

    dp = [float('inf') for _ in range(n)]
    dp[0] = 0
    for i in range(1, n):
        for j in range(max(0, i-k), i):
            dp[i] = min(dp[i], dp[j]+abs(Hs[i]-Hs[j]))

    print(dp[n-1])


if __name__ == '__main__':
    main()
