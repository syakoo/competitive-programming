import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    ABs.sort()

    money = k
    for a, b in ABs:
        if money < a:
            print(money)
            return

        money += b

    print(min(money, 10**100))


if __name__ == '__main__':
    main()
