import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As = lmap(lambda x: x % 200, As)

    cnts = [0] * 200
    for a in As:
        cnts[a] += 1

    ans = 0
    for i in range(200):
        ans += cnts[i] * (cnts[i] - 1) // 2

    print(ans)


if __name__ == '__main__':
    main()
