from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def hw2bit(h: int, w: int) -> int:
    return 1 << (h*4 + w)


def weight(bit: int) -> int:
    cnt = 0
    while bit > 0:
        cnt += bit & 1
        bit >>= 1
    return cnt


def main():
    h, w = 4, 4
    Sss = [list(input()) for _ in range(h)]
    INF = 1 << 10
    bit = 0
    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                bit += hw2bit(hi, wi)

    @lru_cache(None)
    def dfs(bit: int) -> float:
        res = INF
        if weight(bit) == 0:
            return 0

        for hi in range(h):
            for wi in range(w):
                cnt = 0
                ex = 0
                for nh, nw in [(hi-1, wi), (hi+1, wi), (hi, wi), (hi, wi-1), (hi, wi+1)]:
                    if 0 <= nh < h and 0 <= nw < w and hw2bit(nh, nw) & bit:
                        ex += dfs(bit - hw2bit(nh, nw))
                        cnt += 1
                if cnt == 0:
                    continue

                res = min(res, ex/cnt+5/cnt)

        return res

    print(dfs(bit))


if __name__ == '__main__':
    main()
