import math


def lmap(func, iter):
    return list(map(func, iter))


def minmax(t1, t2, t):
    def key(ts): return ts[1] - ts[0]
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    if t == 0:
        return min(t1, t2, key=key)
    else:
        return max(t1, t2, key=key)


def main():
    h, w = map(int, input().split())
    Ass = [input() for _ in range(h)]

    Ass = lmap(lambda As: lmap(lambda a: 1 if a == '+' else -1, As), Ass)
    dp = [[None for _ in range(w)] for _ in range(h)]
    dp[h-1][w-1] = (0, 0)

    for hi in range(h-1, -1, -1):
        for wi in range(w-1, -1, -1):
            if hi < h-1:
                if (hi + wi) % 2 == 0:
                    dp[hi][wi] = minmax(
                        dp[hi][wi], (dp[hi + 1][wi][0], dp[hi + 1][wi][1] + Ass[hi][wi]), 0)
                else:
                    dp[hi][wi] = minmax(
                        dp[hi][wi], (dp[hi + 1][wi][0] + Ass[hi][wi], dp[hi + 1][wi][1]), 1)
            if wi < w-1:
                if (hi + wi) % 2 == 0:
                    dp[hi][wi] = minmax(
                        dp[hi][wi], (dp[hi][wi + 1][0], dp[hi][wi + 1][1] + Ass[hi][wi]), 0)
                else:
                    dp[hi][wi] = minmax(
                        dp[hi][wi], (dp[hi][wi + 1][0] + Ass[hi][wi], dp[hi][wi + 1][1]), 1)

    p1, p2 = dp[0][0]
    if p1 == p2:
        print('Draw')
    elif p1 > p2:
        print('Takahashi')
    else:
        print('Aoki')


if __name__ == '__main__':
    main()
