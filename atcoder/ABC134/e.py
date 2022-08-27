from bisect import bisect_left


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = [int(input()) for _ in range(n)]

    Bs = [-1]*n
    for a in As:
        idx = bisect_left(Bs, a)
        Bs[idx - 1] = a

    print(n - Bs.count(-1))


if __name__ == '__main__':
    main()
