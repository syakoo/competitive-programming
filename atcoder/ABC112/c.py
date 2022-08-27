
from itertools import product
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    XYHs = [lmap(int, input().split()) for _ in range(n)]
    mxXYH = max(XYHs, key=lambda x: x[2])  # O(n)

    # O(mx(Cx)*mx(Cy)*n)
    for cx, cy in product(range(0, 101), repeat=2):
        ch = mxXYH[2] + abs(cx - mxXYH[0]) + abs(cy - mxXYH[1])
        flg = True

        for x, y, h in XYHs:
            if h != max(0, ch - abs(cx - x) - abs(cy - y)):
                flg = False
                break

        if flg:
            print(cx, cy, ch)
            return


if __name__ == '__main__':
    main()
