
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    k, s = map(int, input().split())

    ans = 0
    for x in range(0, k + 1):
        for y in range(0, k + 1):
            if s - k <= x + y <= s:
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
