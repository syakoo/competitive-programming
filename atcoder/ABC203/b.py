import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())

    ans = 0
    for i in range(1, n + 1):
        for j in range(1, k + 1):
            ans += i * 100 + j

    print(ans)


if __name__ == '__main__':
    main()
