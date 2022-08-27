import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s, t = input().split()
    a, b = map(int, input().split())
    u = input()

    if u == s:
        a -= 1
    elif u == t:
        b -= 1

    print(a, b)


if __name__ == '__main__':
    main()
