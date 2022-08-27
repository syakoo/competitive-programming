
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    cnts = [0] * (n + 1)
    for a, b in ABs:
        cnts[a] ^= 1
        cnts[b] ^= 1

    print('YES' if sum(cnts) == 0 else 'NO')


if __name__ == '__main__':
    main()
