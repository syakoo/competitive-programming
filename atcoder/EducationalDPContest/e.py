import math


def main():
    n, w = map(int, input().split())
    Ws = [(0, 0)] + [list(map(int, input().split())) for _ in range(n)]
    max_value = 10**3 * n
    dp = [[math.inf if vi > 0 else 0 for _ in range(
        n + 1)] for vi in range(max_value + 1)]

    for vi in range(1, max_value + 1):
        for ni in range(1, n + 1):
            if Ws[ni][1] > vi:
                dp[vi][ni] = dp[vi][ni-1]
            else:
                dp[vi][ni] = min(
                    dp[vi][ni - 1], dp[vi - Ws[ni][1]][ni - 1] + Ws[ni][0])

    for vi in range(max_value, 0, -1):
        if dp[vi][n] <= w:
            print(vi)
            return


if __name__ == '__main__':
    main()
