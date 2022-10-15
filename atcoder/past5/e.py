import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = lmap(int, input().split())
    Sss = ['#'*(20 + w)]*10 + ['#'*10 + input() + '#' *
                               10 for _ in range(h)] + ['#'*(20 + w)]*10
    Tss = [input() for _ in range(h)]

    def rotate(Xss):
        result = [['']*len(Xss) for _ in range(len(Xss[0]))]

        for hi in range(len(Xss)):
            for wi in range(len(Xss[0])):
                result[wi][-hi-1] = Xss[hi][wi]

        return result

    def check(Xss, Yss, xhi, xwi):
        for hi in range(len(Xss)):
            for wi in range(len(Xss[0])):
                if Xss[hi][wi] == Yss[hi + xhi][wi + xwi] == '#':
                    return False

        return True

    for _ in range(4):
        for bhi in range(len(Sss) - len(Tss)):
            for bwi in range(len(Sss[0]) - len(Tss[0])):
                if check(Tss, Sss, bhi, bwi):
                    print('Yes')
                    return

        Tss = rotate(Tss)

    print('No')


if __name__ == '__main__':
    main()
