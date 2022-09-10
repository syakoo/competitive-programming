# https://algo-method.com/tasks/341
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())

    dp = [-1] * m
    dp[0] = 0
    for i in range(n-1):
        for j in reversed(range(m)):
            if dp[j] != -1 and j+As[i] < m:
                dp[j+As[i]] = max(dp[j+As[i]], dp[j] + Bs[i])

    print(dp[-1])


if __name__ == '__main__':
    main()
