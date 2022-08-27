import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ss = [input() for _ in range(n)]

    print(len(set(Ss)))


if __name__ == '__main__':
    main()
