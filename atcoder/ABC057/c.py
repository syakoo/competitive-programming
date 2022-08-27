# 4 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def find_div(n: int) -> int:
    result = 0
    for x in range(1, int(n**(1/2)) + 1):
        if n % x == 0:
            result = x

    return result


def main():
    n = int(input())
    mx = n // find_div(n)
    print(len(str(mx)))


if __name__ == '__main__':
    main()
