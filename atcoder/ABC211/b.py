import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    Ss = [input() for _ in range(4)]
    if sorted(Ss) == sorted(['H', '2B', '3B', 'HR']):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
