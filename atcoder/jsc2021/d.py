
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, p = map(int, input().split())
    MOD = 10**9 + 7
    print((p - 1) * pow(p - 2, n - 1, MOD) % MOD)


if __name__ == '__main__':
    main()
