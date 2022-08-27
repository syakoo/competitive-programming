def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ts = lmap(int, input().split())

    Tsum = sum(Ts)
    dp = [[0]*(Tsum + 1) for _ in range(n+1)]
    dp[0][0] = 1

    for i in range(n):
        for v in range(Tsum + 1):
            if dp[i][v]:
                dp[i+1][v] = 1
                dp[i+1][v+Ts[i]] = 1

    ans = Tsum
    for v in range(Tsum):
        if dp[-1][v]:
            ans = min(ans, max(v, Tsum-v))

    print(ans)


if __name__ == '__main__':
    main()
