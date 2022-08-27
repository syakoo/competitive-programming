
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [list(input()) for _ in range(h)]
    maps = [[] for _ in range(11)]

    for hi in range(h):
        for wi in range(w):
            a = Ass[hi][wi]
            if a == 'S':
                maps[0].append((hi, wi))
            elif a == 'G':
                maps[-1].append((hi, wi))
            else:
                maps[int(a)].append((hi, wi))

    dp = [[math.inf for _ in range(h*w)] for _ in range(11)]
    dp[0][0] = 0

    for i in range(1, 11):
        for j in range(h*w):
            if dp[i - 1][j] >= math.inf:
                break

            for k in range(len(maps[i])):
                fx, fy = maps[i - 1][j]
                tx, ty = maps[i][k]
                dp[i][k] = min(dp[i][k], dp[i - 1][j] +
                               abs(tx - fx) + abs(ty - fy))

    print(dp[-1][0] if dp[-1][0] < math.inf else -1)


if __name__ == '__main__':
    main()
