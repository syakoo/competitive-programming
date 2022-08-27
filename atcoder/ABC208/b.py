import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    p = int(input())
    coins = []

    for x in range(1, 11):
        s = 1
        for i in range(1, x+1):
            s *= i
        coins.append(s)

    coins.sort(reverse=True)
    cnt = 0
    i = 0
    while p:
        x = min(100, p//coins[i])
        cnt += x
        p -= x*coins[i]
        i += 1

    print(cnt)


if __name__ == '__main__':
    main()
