import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())

    if c % 2 == 0:
        a = abs(a)
        b = abs(b)

    if a >= 0 and b >= 0:
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')
        return
    elif a >= 0 and b < 0:
        print('>')
    elif a < 0 and b >= 0:
        print('<')
    else:
        if a > b:
            print('>')
        elif a < b:
            print('<')
        else:
            print('=')
        return


if __name__ == '__main__':
    main()
