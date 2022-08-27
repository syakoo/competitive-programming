# 4 min 24 sec

from itertools import permutations
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    XYs = [lmap(int, input().split()) for _ in range(n)]
    allsum = 0
    cnt = 0

    for xys in permutations(XYs):
        cnt += 1
        x, y = xys[0]
        for x2, y2 in xys[1:]:
            allsum += math.sqrt((x - x2)**2 + (y - y2)**2)
            x, y = x2, y2

    print(allsum / cnt)


if __name__ == '__main__':
    main()
