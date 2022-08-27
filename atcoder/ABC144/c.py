
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ans = 10**12

    for x in range(1, int(n**(1/2)) + 1):
        if n % x == 0:
            ans = min(ans, x + (n // x))

    print(ans - 2)


if __name__ == '__main__':
    main()
