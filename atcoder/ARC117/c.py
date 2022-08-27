
from operator import mul
from functools import reduce
from collections import deque
import math


def lmap(func, iter):
    return list(map(func, iter))


def cmb(n, r):
    r = min(n-r, r)
    if r == 0:
        return 1
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


def modinv(x):
    return x


def binomial_coefficients(n, k):
    numera = 1
    denomi = 1

    for i in range(k):
        numera *= n-i
        numera %= 3
        denomi *= i+1
        denomi %= 3
    return numera * modinv(denomi) % 3


def main():
    n = int(input())
    C = input()
    Cs = []
    for c in C:
        if c == 'B':
            Cs.append(0)
        elif c == 'R':
            Cs.append(1)
        else:
            Cs.append(2)

    ans = 0
    for i, c in enumerate(Cs):
        ans += binomial_coefficients(n-1, i)*c % 3

    if n % 2 == 0:
        ans = - ans
    ans %= 3

    if ans == 0:
        print('B')
    elif ans == 1:
        print('R')
    else:
        print('W')


if __name__ == '__main__':
    main()
