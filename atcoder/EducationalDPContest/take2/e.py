import itertools as it


def lmap(func, iter):
    return list(map(func, iter))


def main():
    N, W = map(int, input().split())
    WVs = [lmap(int, input().split()) for _ in range(N)]

    V = 1000*N
    INF = W+1
    dp = [[INF for _ in range(V+1)] for _ in range(N+1)]
    dp[0][0] = 0
    for i in range(N):
        w, v = WVs[i]
        for j in range(V+1):
            dp[i+1][j] = min(dp[i+1][j], dp[i][j])
            if j - v >= 0:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j-v]+w)

    print(len(list(it.dropwhile(lambda x: x > W, reversed(dp[-1]))))-1)


if __name__ == '__main__':
    main()
