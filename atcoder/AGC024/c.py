import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]

    if As[0] != 0:
        print(-1)
        return

    l = 0
    ans = 0
    for i in range(n - 1):
        if As[i] == 0:
            if As[i + 1] > 1:
                print(-1)
                return

        li = i+1 - As[i+1] + 1
        if li < l:
            print(-1)
            return
        elif li != l:
            ans += As[i]

        l = li

    print(ans + As[-1])


if __name__ == '__main__':
    main()
