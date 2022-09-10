import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    Ns = lmap(int, input().split())
    print(len(set(Ns)))


if __name__ == '__main__':
    main()
