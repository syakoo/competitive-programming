import math
import sys
from itertools import permutations

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ps = ''.join(input().split())
    Qs = ''.join(input().split())
    li = list(permutations(range(1, n + 1)))
    li = lmap(lambda xs: ''.join(map(str, xs)), li)
    li.sort()

    print(abs(li.index(Ps) - li.index(Qs)))


if __name__ == '__main__':
    main()
