import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def sumcmb2(n: int):
    return (n*(n+1)//2 + n*(n+1)*(2*n + 1)//6) // 2


def main():
    n, k = map(int, input().split())

    l, r = 3, n**3
    while r - l > 1:
        m = (r + l) // 2
        if sumcmb2(m - 2) > k:
            r = m
        else:
            l = m

    if sumcmb2(l - 2) < k:
        li = l
    else:
        li = r

    cnt = sumcmb2(li)
    l, r = li, sumcmb2(li + 1)
    while r - l > 1:
        m = (r + l) // 2

    print(li)
    print(lmap(lambda x: sumcmb2(x - 2), range(n**3)))


if __name__ == '__main__':
    main()
