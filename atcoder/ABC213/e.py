from itertools import product
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    INF = -1

    dXYs = list(filter(lambda xy: not xy[0] == xy[1] == 0 and not abs(
        xy[0]) == abs(xy[1]) == 2, product(range(-2, 3), repeat=2)))
    q1 = deque([(0, 0)])
    costs = [[INF]*w for _ in range(h)]
    costs[0][0] = 0

    for i in range(max(h, w)):
        q2 = deque([])
        while q1:
            hi, wi = q1.popleft()
            q2.append((hi, wi))
            if (hi, wi) == (h-1, w-1):
                print(i)
                return

            for dh, dw in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nh, nw = hi + dh, wi + dw
                if 0 <= nh < h and 0 <= nw < w and Sss[nh][nw] == '.' and costs[nh][nw] == INF:
                    costs[nh][nw] = i
                    q1.append((nh, nw))

        while q2:
            hi, wi = q2.popleft()

            for dh, dw in dXYs:
                nh, nw = hi + dh, wi + dw
                if 0 <= nh < h and 0 <= nw < w and costs[nh][nw] == INF:
                    costs[nh][nw] = i + 1
                    q1.append((nh, nw))

    return costs[-1][-1]


if __name__ == '__main__':
    main()
