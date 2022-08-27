import math


def lmap(func, iter):
    return list(map(func, iter))


def jadge(n: int, k: int, As: list) -> bool:
    cnt = 0
    for a in As:
        cnt += math.ceil(a / n) - 1
        if cnt > k:
            return False

    return True


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    l, r = 1, max(As)
    while r - l > 1:
        m = (r + l) // 2
        if jadge(m, k, As):
            r = m
        else:
            l = m

    if jadge(l, k, As):
        print(l)
    else:
        print(l + 1)


if __name__ == '__main__':
    main()
