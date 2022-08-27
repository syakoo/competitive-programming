import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    x = (108*n)//100
    if x == 206:
        print('so-so')
    elif x < 206:
        print('Yay!')
    else:
        print(':(')


if __name__ == '__main__':
    main()
