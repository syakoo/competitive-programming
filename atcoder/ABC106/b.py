import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    ans = 0
    for x in range(1, n+1, 2):
        cnt = 0
        for i in range(1, x+1):
            if x % i == 0:
                cnt += 1

        if cnt == 8:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
