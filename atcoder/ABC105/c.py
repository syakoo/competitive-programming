# 34 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def sum_pos(n: int) -> int:
    if n < 0:
        return 0
    if n % 2 == 1:
        n -= 1
    return (pow(2, n + 2) - 1) // 3


def sum_neg(n: int) -> int:
    if n < 0:
        return 0
    if n % 2 == 1:
        n += 1
    return (-2 * pow(2, n) + 2) // 3


def main():
    n = int(input())

    k = 0
    while not(sum_neg(k) <= n <= sum_pos(k)):
        k += 1

    ans = []
    for ki in range(k, -1, -1):
        if not(sum_neg(ki - 1) <= n <= sum_pos(ki - 1)):
            ans.append('1')
            n -= pow(-2, ki)
        else:
            ans.append('0')

    print(''.join(ans))


if __name__ == '__main__':
    main()
