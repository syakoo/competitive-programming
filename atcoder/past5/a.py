import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    ss = input()

    if 'ooo' in ss:
        print('o')
        return
    elif 'xxx' in ss:
        print('x')
        return

    print('draw')


if __name__ == '__main__':
    main()
