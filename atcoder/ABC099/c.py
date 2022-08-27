# not cleared

def lmap(func, iter):
    return list(map(func, iter))


INF = 10**5


def main():
    n = int(input())
    dp = [INF]*(n + 1)
    dp[0] = 0
    ls = [1, 6, 9, 36, 81, 216, 729, 1296, 6561, 7776, 59049]

    for i in range(1, n + 1):
        for l in ls:
            if l > i:
                continue
            dp[i] = min(dp[i], dp[i - l] + 1)

    print(dp[n])


if __name__ == '__main__':
    main()
