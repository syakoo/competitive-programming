import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    NTs = [input().split() for _ in range(n)]
    NTs.sort(key=lambda nt: int(nt[1]), reverse = True)

    print(NTs[1][0])


if __name__ == '__main__':
    main()
