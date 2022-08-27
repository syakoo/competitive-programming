import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c, x, y = map(int, input().split())
    both_min = min(a + b, 2*c) * min(x, y)

    if x > y:
        ans = both_min + min(a, 2*c) * abs(x - y)
    else:
        ans = both_min + min(b, 2*c) * abs(x - y)

    print(ans)


if __name__ == '__main__':
    main()
