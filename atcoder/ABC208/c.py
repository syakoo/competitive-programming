import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    m, r = divmod(k, n)
    Bs = sorted(As)
    Cs = dict((b, i) for i, b in enumerate(Bs))
    As = lmap(lambda a: Cs[a], As)
    As = lmap(lambda a: m if r <= a else m + 1, As)

    print('\n'.join(map(str, As)))


if __name__ == '__main__':
    main()
