# 6 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]

    ans = 0
    for i in range(n):
        ans += As[i] // 2
        As[i] %= 2

        if i < n - 1 and As[i] == 1 and As[i+1] > 0:
            As[i+1] -= 1
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
