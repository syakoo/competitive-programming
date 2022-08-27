import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())

    for _ in range(k):
        if n % 200 == 0:
            n //= 200
        else:
            n = n*1000+200

    print(n)


if __name__ == '__main__':
    main()
