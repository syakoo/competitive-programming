import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    ABC = lmap(int, input().split())
    ABC.sort()
    print(ABC[1] + ABC[2])


if __name__ == '__main__':
    main()
