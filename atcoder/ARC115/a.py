
import math


def lmap(func, iter):
    return list(map(func, iter))


def dist(xs: str, ys: str):
    cnt = 0
    for x, y in zip(xs, ys):
        if x != y:
            cnt += 1

    return cnt


def main():
    n, m = map(int, input().split())
    Ss = [input() for _ in range(n)]
    d_from1 = [0] * 2

    for i in range(1, n):
        d_from1[dist(Ss[0], Ss[i]) % 2] += 1

    print(d_from1[1] + d_from1[0] * d_from1[1])


if __name__ == '__main__':
    main()
