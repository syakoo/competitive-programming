def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    dp = [[[0]*(n+2) for _ in range(n+2)] for _ in range(n+2)]

    cnts = [0]*3
    for a in As:
        if a > 0:
            cnts[a - 1] += 1

    for i3 in range(cnts[2] + 1):
        for i2 in range(cnts[1] + cnts[2] + 1 - i3):
            for i1 in range(sum(cnts) + 1 - i3 - i2):
                sm = i1 + i2 + i3
                if sm == 0:
                    continue

                dp[i1][i2][i3] = n / sm
                if i1:
                    dp[i1][i2][i3] += dp[i1 - 1][i2][i3] * (i1 / sm)
                if i2:
                    dp[i1][i2][i3] += dp[i1 + 1][i2 - 1][i3] * (i2 / sm)
                if i3:
                    dp[i1][i2][i3] += dp[i1][i2 + 1][i3 - 1] * (i3 / sm)

    print(dp[cnts[0]][cnts[1]][cnts[2]])


if __name__ == '__main__':
    main()
