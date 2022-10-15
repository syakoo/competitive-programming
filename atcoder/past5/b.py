import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ss = input()

    t = ''
    for s in ss:
        t = t.replace(s, '')
        t += s

    print(t)


if __name__ == '__main__':
    main()
