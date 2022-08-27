import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c, d = map(int, input().split())
    ta, tb = math.ceil(c / b), math.ceil(a / d)

    if ta <= tb:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()
