
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())
    Acnts = [0]*n

    for a in As:
        Acnts[a] += 1

    mx = min(n, k)
    ans = 0
    for Acnt in Acnts:
        mx = min(mx, Acnt)
        ans += mx

    print(ans)


if __name__ == '__main__':
    main()
