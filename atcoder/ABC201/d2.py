import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [input() for _ in range(h)]

    pss = [[0]*(w+1) for _ in range(h + 1)]
    for hi in range(h):
        for wi in range(w):
            if Ass[hi][wi] == '+':
                pss[hi][wi] = 1
            else:
                pss[hi][wi] = -1
    dp = [[math.inf if (wi + hi) % 2 == 0 else
           -math.inf for wi in range(w + 1)] for hi in range(h + 1)]
    dp[h-1][w-1] = 0

    for hi in range(h-1, -1, -1):
        for wi in range(w-1, -1, -1):
            if hi == h-1 and wi == w-1:
                continue

            if (hi + wi) % 2 == 0:
                dp[hi][wi] = max(dp[hi + 1][wi] + pss[hi + 1][wi],
                                 dp[hi][wi + 1] + pss[hi][wi + 1])
            else:
                dp[hi][wi] = min(dp[hi + 1][wi] - pss[hi + 1][wi],
                                 dp[hi][wi + 1] - pss[hi][wi + 1])

    if dp[0][0] == 0:
        print('Draw')
    elif dp[0][0] > 0:
        print('Takahashi')
    else:
        print('Aoki')


if __name__ == '__main__':
    main()
