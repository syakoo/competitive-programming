import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    print('YES' if len(set(As)) == n else 'NO')


if __name__ == '__main__':
    main()
