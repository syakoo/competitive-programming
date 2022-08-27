import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As = lmap(lambda x: x % 30001, input().split())

    for i in range(1, n+1):
        pass


if __name__ == '__main__':
    main()
