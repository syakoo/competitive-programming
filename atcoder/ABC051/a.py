
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    print(' '.join(s.split(',')))


if __name__ == '__main__':
    main()
