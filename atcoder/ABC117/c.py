def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    Xs = lmap(int, input().split())

    if n >= m:
        print(0)
        return

    Xs.sort()
    subXs = lmap(lambda ps: abs(ps[0] - ps[1]), zip(Xs, Xs[1:]))
    subXs.sort()
    print(sum(subXs[:m-n]))


if __name__ == '__main__':
    main()
