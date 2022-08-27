import math
from functools import reduce


def lmap(func, iter):
    return list(map(func, iter))


def dist(p1: list, p2: list) -> int:
    return (p1[0] - p2[0])**2 + (p1[1] - p2[1])**2


def radians(coords: list) -> list:
    return lmap(lambda xs: (dist(xs, (0, 0)), math.degrees(math.atan2(xs[1], xs[0]))), coords)


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    CDs = [lmap(int, input().split()) for _ in range(n)]

    ABo = reduce(lambda prev, xs: (prev[0]+xs[0], prev[1]+xs[1]), ABs)
    CDo = reduce(lambda prev, xs: (prev[0]+xs[0], prev[1]+xs[1]), CDs)

    ABs = lmap(lambda xs: (xs[0]*n - ABo[0], xs[1]*n - ABo[1]), ABs)
    CDs = lmap(lambda xs: (xs[0]*n - CDo[0], xs[1]*n - CDo[1]), CDs)
    if (0, 0) in ABs:
        if (0, 0) not in CDs:
            print('No')
            return
    else:
        if (0, 0) in CDs:
            print('No')
            return
    ABs = list(filter(lambda xs: (xs[1], xs[0]) != (0, 0), ABs))
    CDs = list(filter(lambda xs: (xs[1], xs[0]) != (0, 0), CDs))

    ABrads = radians(ABs)
    CDrads = radians(CDs)
    ABrads.sort(key=lambda xs: (xs[1], xs[0]))
    CDrads.sort(key=lambda xs: (xs[1], xs[0]))
    ABrads += ABrads
    e = 0.00001

    for li in range(n):
        flg = True
        for ab, cd in zip(ABrads[li:], CDrads):
            if abs((ab[1] - ABrads[li][1]) % 360 - (cd[1] - CDrads[0][1]) % 360) > e or abs(ab[0] - cd[0]) > e:
                flg = False
                break

        if flg:
            print('Yes')
            return

    print('No')


if __name__ == '__main__':
    main()
