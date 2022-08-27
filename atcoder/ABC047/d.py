from collections import defaultdict


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, t = map(int, input().split())
    As = lmap(int, input().split())

    mn = 1 << 60
    benes = defaultdict(int)
    for a in As:
        mn = min(mn, a)
        benes[a-mn] += 1

    print(benes[max(benes.keys())])


if __name__ == '__main__':
    main()
