import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    dp = [0] * (k + 1)
    for i in range(1, k+1):
        for a in As:
            if i - a < 0:
                break

            dp[i] |= dp[i - a] ^ 1

    print('First' if dp[k] else 'Second')


if __name__ == '__main__':
    main()
