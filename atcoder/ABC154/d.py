import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ps = lmap(int, input().split())
    ps = lmap(lambda x: (x*(x + 1)//2)/x, ps)

    e = sum(ps[:k])
    ans = e
    for l in range(1, n - k + 1):
        r = l + k - 1
        e += ps[r] - ps[l - 1]
        ans = max(ans, e)

    print(ans)


if __name__ == '__main__':
    main()
