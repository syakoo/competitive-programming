# 13 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, d = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(h)]
    q = int(input())
    LRs = [lmap(int, input().split()) for _ in range(q)]

    cells = [None]*(h*w + 1)
    for hi in range(h):
        for wi in range(w):
            cells[Ass[hi][wi]] = (hi, wi)

    depths = [0] * (h*w + 1)
    for x in range(d + 1, h*w + 1):
        dist = abs(cells[x][0] - cells[x - d][0]) + \
            abs(cells[x][1] - cells[x - d][1])
        depths[x] = depths[x - d] + dist

    for l, r in LRs:
        print(depths[r] - depths[l])


if __name__ == '__main__':
    main()
