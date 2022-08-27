# 8 min
import math


def lmap(func, iter):
    return list(map(func, iter))


def abst(s: str) -> list:
    sset = set(list(s))
    sdict = dict((s, i) for i, s in enumerate(sset))
    result = []

    for si in s:
        result.append(sdict[si])

    return result


def main():
    s = input()
    t = input()

    print('Yes' if abst(s) == abst(t) else 'No')


if __name__ == '__main__':
    main()
