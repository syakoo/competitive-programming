def main():
    n, k = map(int, input().split())
    H = list(map(int, input().split()))
    dp = [0 for _ in range(n)]
    dp[1] = abs(H[0] - H[1])

    for ni in range(2, n):
        dp[ni] = min([dp[ni-ki] + abs(H[ni] - H[ni-ki])
                      for ki in range(1, min(k, ni) + 1)])

    print(dp[n - 1])


if __name__ == '__main__':
    main()
