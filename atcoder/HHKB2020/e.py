# 31 min

import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    hlmps = [[0 for _ in range(w)] for _ in range(h)]
    wlmps = [[0 for _ in range(w)] for _ in range(h)]
    MOD = 10**9 + 7
    k = 0

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                continue
            k += 1

            if hi == 0 or Sss[hi - 1][wi] == '#':
                nh, nw = hi, wi

                while 0 <= nh < h and 0 <= nw < w and Sss[nh][nw] != '#':
                    hlmps[hi][wi] += 1
                    nh += 1
            else:
                hlmps[hi][wi] = hlmps[hi - 1][wi]

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                continue

            if wi == 0 or Sss[hi][wi - 1] == '#':
                nh, nw = hi, wi

                while 0 <= nh < h and 0 <= nw < w and Sss[nh][nw] != '#':
                    wlmps[hi][wi] += 1
                    nw += 1
            else:
                wlmps[hi][wi] = wlmps[hi][wi - 1]

    ans = (k * pow(2, k, MOD)) % MOD
    for hi in range(h):
        for wi in range(w):
            if hlmps[hi][wi] + wlmps[hi][wi]:
                ans -= pow(2, k-(hlmps[hi][wi] + wlmps[hi][wi] - 1), MOD)
                ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
