import sys
from collections import defaultdict

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    S = lmap(int, input())[::-1]
    rs = [0]*2019
    rs[0] = 1

    r = 0
    for si, sv in enumerate(S):
        r += pow(10, si, 2019) * sv
        r %= 2019
        rs[r] += 1

    ans = 0
    for r in rs:
        ans += r*(r-1) // 2

    print(ans)


if __name__ == '__main__':
    main()
