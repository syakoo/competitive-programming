import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    XYs = [lmap(int, input().split()) for _ in range(n)]

    Xs = []
    Ys = []
    for i, (x, y) in enumerate(XYs):
        Xs.append((x, i))
        Ys.append((y, i))

    Xs.sort()
    Ys.sort()

    print(Xs, Ys)
    if (Xs[0][1] == Ys[0][1] and Xs[-1][1] == Ys[-1][1]) or (Xs[0][1] == Ys[-1][1] and Xs[-1][1] == Ys[0][1]):
        print(max(Xs[-1][0] - Xs[1][0], Xs[-2][0] - Xs[0][0],
                  Ys[-1][0] - Ys[1][0], Ys[-2][0] - Ys[0][0]))
    else:
        ans = min(Xs[-1][0] - Xs[0][0], Ys[-1][0] - Ys[0][0])


if __name__ == '__main__':
    main()
