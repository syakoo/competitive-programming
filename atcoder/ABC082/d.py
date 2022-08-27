import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def solve(xs: list, p: int) -> bool:
    sumxs = sum(xs)
    if sumxs < abs(p):
        return False
    elif sumxs == abs(p):
        return True

    m, r = sumxs, 2 * sumxs
    dp = [[0 for _ in range(r + 1)] for _ in range(len(xs) + 1)]
    dp[0][m] = 1

    for i in range(1, len(xs) + 1):
        for j in range(r + 1):
            if 0 <= j - xs[i - 1]:
                dp[i][j] |= dp[i-1][j-xs[i - 1]]

            if j + xs[i - 1] <= r:
                dp[i][j] |= dp[i - 1][j+xs[i - 1]]

    return bool(dp[len(xs)][p + m])


def main():
    s = input()
    x, y = map(int, input().split())

    direct = 0
    ys = []
    xs = []
    cnt = 0
    for c in s:
        if c == 'F':
            cnt += 1
        else:
            if direct:
                ys.append(cnt)
            else:
                xs.append(cnt)

            direct ^= 1
            cnt = 0
    if direct:
        ys.append(cnt)
    else:
        xs.append(cnt)

    pos = (0, 0)
    if s[0] == 'F':
        pos = (xs[0], 0)
        xs = xs[1:]

    if solve(ys, y) and solve(xs, x - pos[0]):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
