import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c, d, e, f = map(int, input().split())

    mx = 0
    ans = (0, 0)
    for ai in range(31):
        if a*ai*100 > f:
            continue
        for bi in range(31):
            if ai == bi == 0:
                continue
            if a*ai*100 + b*bi*100 > f:
                break
            water = a*ai*100 + b*bi*100
            for ci in range(3001):
                if water + c*ci > f:
                    break

                y = water * e / 100
                di = min(y - c*ci, f - water - c * ci) // d
                di = int(di)
                sugar = c*ci + d*di
                if di >= 0:
                    if mx < sugar / (water + sugar):
                        ans = (water + sugar, sugar)
                        mx = sugar / (water + sugar)

    if ans[0] == 0:
        print(a*100, 0)
    else:
        print(*ans)


if __name__ == '__main__':
    main()
