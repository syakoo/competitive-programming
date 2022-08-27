# 6 min
from itertools import accumulate
from bisect import *


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    ABs.sort()

    Aacums = [0] + list(accumulate(map(lambda xs: xs[1], ABs)))
    idx = bisect_left(Aacums, k)
    print(ABs[idx - 1][0])


if __name__ == '__main__':
    main()
