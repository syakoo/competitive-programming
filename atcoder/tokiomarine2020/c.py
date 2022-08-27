import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    for _ in range(k):
        tmp = [0]*n
        for i in range(n):
            tmp[max(0, i - As[i])] += 1
            if i + As[i] + 1 < n:
                tmp[i + As[i] + 1] -= 1

        flg = True
        for i in range(1, n):
            tmp[i] += tmp[i - 1]
            if tmp[i] != n:
                flg = False

        if flg:
            print(*tmp)
            return

        As = tmp

    print(*As)


if __name__ == '__main__':
    main()
