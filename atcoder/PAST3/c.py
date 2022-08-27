import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, r, n = map(int, input().split())
    if (n - 1) * math.log10(r) > 9:
        print('large')
        return

    an = a * pow(r, n - 1)
    if an > 10**9:
        print('large')
        return

    print(an)


if __name__ == '__main__':
    main()
