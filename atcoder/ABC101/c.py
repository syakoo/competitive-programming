def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    idx = As.index(1)
    l = idx
    r = n - idx - 1
    ll, lr = divmod(l, k-1)
    print(ll + -(-(r + lr)//(k-1)))


if __name__ == '__main__':
    main()
