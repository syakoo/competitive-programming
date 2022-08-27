
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Ass = [input() for _ in range(h)]
    rowidxs = set()
    colidxs = set()

    for hi in range(h):
        for wi in range(w):
            if Ass[hi][wi] == '#':
                rowidxs.add(hi)
                colidxs.add(wi)

    for hi in range(h):
        if hi not in rowidxs:
            continue
        for wi in range(w):
            if wi in colidxs:
                print(Ass[hi][wi], end='')

        print()


if __name__ == '__main__':
    main()
