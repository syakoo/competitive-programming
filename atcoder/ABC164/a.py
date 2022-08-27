import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s, w = map(int, input().split())
    print('unsafe' if s <= w else 'safe')


if __name__ == '__main__':
    main()
