import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    alphas = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    if n == 0:
        print(0)
        return

    result = ''
    while n > 0:
        result = alphas[n % 36] + result
        n //= 36

    print(result)


if __name__ == '__main__':
    main()
