import math
import sys
from collections import deque

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x, y = lmap(int, input().split())
    XYs = [lmap(int, input().split()) for _ in range(n)]

    mxh, mxw = 400 + 3, 400 + 3
    bh, bw = 201, 201
    _map = [[0]*mxh for _ in range(mxw)]

    for xi, yi in XYs:
        _map[yi + bh][xi + bw] = -1

    movements = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 0)]
    q = deque([(bh, bw)])
    while q:
        hi, wi = q.popleft()

        for dh, dw in movements:
            nh, nw = hi + dh, wi + dw
            if 0 <= nh < mxh and 0 <= nw < mxw and _map[nh][nw] == 0:
                _map[nh][nw] = _map[hi][wi] + 1
                q.append((nh, nw))

    if _map[y + bh][x + bw] >= 1:
        print(_map[y + bh][x + bw])
    else:
        print(-1)


if __name__ == '__main__':
    main()
