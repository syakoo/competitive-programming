import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, a, x, y = map(int, input().split())

    if a < n:
        ans = x*a + (n - a)*y
    else:
        ans = x*n
    print(ans)


if __name__ == '__main__':
    main()
