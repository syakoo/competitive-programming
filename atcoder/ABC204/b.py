import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    ans = 0
    for a in As:
        ans += max(0, a - 10)

    print(ans)


if __name__ == '__main__':
    main()
