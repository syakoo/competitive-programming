import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    xs = input()

    if len(set(xs)) == 1 or all((int(x1) + 1) % 10 == int(x2) for x1, x2 in zip(xs, xs[1:])):
        print('Weak')
    else:
        print('Strong')


if __name__ == '__main__':
    main()
