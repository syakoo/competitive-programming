import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ls = lmap(int, input().split())
    lmax = max(Ls)

    if lmax*2 < sum(Ls):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
