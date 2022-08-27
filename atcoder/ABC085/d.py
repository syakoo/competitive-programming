import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, h = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n)]

    ans = 0
    ABs.sort(key=lambda xs: xs[1], reverse=True)
    a_mx = max(ABs, key=lambda xs: xs[0])[0]

    for a, b in ABs:
        if b > a_mx:
            h -= b
            ans += 1
        else:
            ans += math.ceil(h / a_mx)
            h = 0

        if h <= 0:
            break
    if h > 0:
        ans += math.ceil(h / a_mx)

    print(ans)


if __name__ == '__main__':
    main()
