import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def fib(a: int, b: int, x: int) -> list:
    i = 0
    while a+b < x:
        tmp = a
        a = b
        b += tmp
        i += 1

    return (b, i)


def main():
    n = int(input())
    print(fib(0, 1, n))


if __name__ == '__main__':
    main()
