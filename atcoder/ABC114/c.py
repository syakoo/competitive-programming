# 10 min

from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    l357 = ['3', '5', '7']
    cnt = 0

    for i in range(3, 10):
        for l in product(*[l357]*i):
            if set(l) == set(l357) and int(''.join(l)) <= n:
                cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
