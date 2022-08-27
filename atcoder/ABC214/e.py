import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def check(LRs: list) -> bool:
    return False


def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        LRs = [lmap(int, input().split()) for _ in range(n)]

        if check(LRs):
            print('Yes')
        else:
            print('No')


if __name__ == '__main__':
    main()
