from itertools import product
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    ans_set = set('.')

    for si in range(len(s)):
        ans_set.add(s[si])

        if len(s) - si > 1:
            for t in product(s[si]+'*', s[si + 1]+'*'):
                ans_set.add(t)
        if len(s) - si > 2:
            for t in product(s[si]+'*', s[si + 1]+'*', s[si + 2]+'*'):
                ans_set.add(t)

    print(len(ans_set))


if __name__ == '__main__':
    main()
