
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = input()

    dp = (0, 0)
    for ni in n[::-1]:
        val = int(ni)
        a, b = dp
        if dp[0] == 0:
            dp = (val, 11 - val)
        else:
            dp = (min(a + val, b + val), min(a + 11 - val, b - 1 + 11 - (val + 1)))

    print(min(dp))


if __name__ == '__main__':
    main()
