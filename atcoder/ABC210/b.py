import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = input()
    i = s.index('1')

    if i % 2:
        print('Aoki')
    else:
        print('Takahashi')


if __name__ == '__main__':
    main()
