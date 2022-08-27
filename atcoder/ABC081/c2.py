from collections import Counter
from functools import reduce


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    cnts = Counter(As)
    sides = []
    for v, c in cnts.items():
        for _ in range(c//2):
            sides.append(v)

    sides.sort(reverse=True)

    if len(sides) < 2:
        print(0)
    else:
        print(sides[0]*sides[1])


if __name__ == '__main__':
    main()
