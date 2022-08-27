
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ss = [input() for _ in range(n)]
    cnts = {}

    for s in Ss:
        if s in cnts:
            cnts[s] += 1
        else:
            cnts[s] = 1

    cnts = list(cnts.items())
    cnts.sort(key=lambda x: x[1], reverse=True)
    cnts = list(filter(lambda x: x[1] == cnts[0][1], cnts))
    cnts.sort()

    print('\n'.join(cnt[0] for cnt in cnts))


if __name__ == '__main__':
    main()
