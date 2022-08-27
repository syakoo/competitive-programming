import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    mins = [n]*n
    for a, b in ABs:
        mins[a - 1] = min(mins[a - 1], b - 1)

    mn = n
    ans = 0
    for i, mi in enumerate(mins):
        if mn == i:
            ans += 1
            mn = mi
        else:
            mn = min(mn, mi)

    print(ans)


if __name__ == '__main__':
    main()
