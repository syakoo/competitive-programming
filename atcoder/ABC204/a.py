import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y = map(int, input().split())

    if x == y:
        print(x)
    else:
        if sorted([x, y]) == [0, 1]:
            print(2)
        if sorted([x, y]) == [1, 2]:
            print(0)
        if sorted([x, y]) == [0, 2]:
            print(1)


if __name__ == '__main__':
    main()
