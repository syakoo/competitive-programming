
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    ans = 0

    print(max(0, min(Bs) - max(As) + 1))


if __name__ == '__main__':
    main()
