import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Hs = lmap(int, input().split()) + [0]

    dp = [float('inf')]*(n+1)
    dp[0] = 0
    for i in range(n-1):
        dp[i+1] = min(dp[i+1], dp[i]+abs(Hs[i]-Hs[i+1]))
        dp[i+2] = min(dp[i+2], dp[i]+abs(Hs[i]-Hs[i+2]))

    print(dp[n-1])


if __name__ == '__main__':
    main()
