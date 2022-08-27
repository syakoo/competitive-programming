# 14 min
from bisect import bisect_right


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, d, a = map(int, input().split())
    XHs = [lmap(int, input().split()) for _ in range(n)]

    XHs.sort()
    Xs = lmap(lambda xs: xs[0], XHs)
    cnts = [0]*(n+2)
    ans = 0
    for i, (x, h) in enumerate(XHs):
        cnts[i+1] += cnts[i]
        hp = h - cnts[i+1]

        if hp <= 0:
            continue

        ri = bisect_right(Xs, x+2*d)
        cnt = -(-hp//a)
        ans += cnt
        cnts[i+1] += cnt*a
        cnts[ri+1] -= cnt*a

    print(ans)


if __name__ == '__main__':
    main()
