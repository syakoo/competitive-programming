import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c, d = map(int, input().split())
    if c*d <= b:
        print(-1)
        return

    x = a / (c*d - b)
    print(math.ceil(x))


if __name__ == '__main__':
    main()
