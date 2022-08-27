import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, d, h = map(int, input().split())
    DHs = [lmap(int, input().split()) for _ in range(n)]
    DHs.sort(key=lambda x: x[0])
    ans = 0

    for i, dh in enumerate(DHs):
        d1, h1 = dh
        a = (h - h1) / (d - d1) 
        b = h1 - a*d1

        ans = max(ans, b)

    print(ans)


if __name__ == '__main__':
    main()
