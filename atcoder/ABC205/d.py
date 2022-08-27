from bisect import bisect_left


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, q = map(int, input().split())
    As = lmap(int, input().split())
    Ks = [int(input()) for _ in range(q)]

    As.sort()
    for k in Ks:
        l, r = 1, 10**20
        while r - l > 1:
            m = (r+l)//2
            idx = bisect_left(As, m)
            if m - idx > k:
                r = m
            else:
                l = m

        print(l)


if __name__ == '__main__':
    main()
