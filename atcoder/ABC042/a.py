
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    ABC = lmap(int, input().split())
    ABC.sort()

    if ABC[0] == ABC[1] == 5 and ABC[2] == 7:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
