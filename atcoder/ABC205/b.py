import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As.sort()

    for i, a in enumerate(As):
        if a != i+1:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
