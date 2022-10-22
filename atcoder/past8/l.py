from itertools import accumulate
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())
    sumAs = [0] + list(accumulate(As))
    sumAs.sort()

    def check(s: int) -> bool:
        r = 0
        l = 0
        cnt = 0
        for m in range(n + 1):
            while r < n + 1 and abs(sumAs[r] - sumAs[m]) < s:
                r += 1

            while l < n + 1 and abs(sumAs[l] - sumAs[m]) >= s:
                l += 1

            cnt += r - l - 1

            if cnt >= k*2:
                return True

        return False

    l, r = 0, 10 ** 15
    while r - l > 1:
        c = (r + l) // 2

        if check(c):
            r = c
        else:
            l = c

    print(l)


if __name__ == '__main__':
    main()
