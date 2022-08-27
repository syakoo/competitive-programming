def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABCs = [lmap(int, input().split()) for _ in range(n)]

    dp = [[0]*3 for _ in range(n+1)]
    for i in range(n):
        for j in range(3):
            dp[i+1][j] = max(dp[i][(j+1) % 3], dp[i][(j+2) % 3]) + ABCs[i][j]

    print(max(dp[-1]))


if __name__ == '__main__':
    main()
