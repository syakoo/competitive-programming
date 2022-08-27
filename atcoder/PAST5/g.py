import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    cnt = sum(Ss.count('#') for Ss in Sss)

    used = [[0]*w for _ in range(h)]

    def dfs(ps: list, d: int) -> list:
        if d == cnt:
            return [ps]

        hi, wi = ps
        used[hi][wi] = 1
        for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            nh, nw = hi + dh, wi + dw
            if 0 <= nh < h and 0 <= nw < w and Sss[nh][nw] == '#' and used[nh][nw] == 0:
                res = dfs((nh, nw), d+1)
                if d + len(res) == cnt:
                    used[hi][wi] = 0
                    return [ps] + res

        used[hi][wi] = 0
        return []

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                used[hi][wi] = 1
                res = dfs((hi, wi), 1)
                used[hi][wi] = 0
                if len(res) == cnt:
                    print(cnt)
                    print('\n'.join(f'{hi+1} {wi+1}' for hi, wi in res))
                    return


if __name__ == '__main__':
    main()
