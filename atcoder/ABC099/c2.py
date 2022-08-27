def main():
    n = int(input())
    dp = [1 << 60]*(n + 1)
    dp[0] = 0

    coins = [1]
    for x in range(9):
        coins.append(6**x)
        coins.append(9**x)

    for c in coins:
        for x in range(0, n - c + 1):
            dp[x+c] = min(dp[x+c], dp[x] + 1)

    print(dp[-1])


if __name__ == '__main__':
    main()
