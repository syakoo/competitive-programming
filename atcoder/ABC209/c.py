import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Cs = lmap(int, input().split())
    MOD = 10**9 + 7
    Cs.sort()

    ans = 1
    for i, c in enumerate(Cs):
        ans *= (c - i)
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
