
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    k = int(input())
    xm = 7 % k
    i = 0
    S = set()

    while xm not in S:
        S.add(xm)
        i += 1
        if xm == 0:
            print(i)
            return

        xm = (xm * 10 + 7) % k

    print(-1)


if __name__ == '__main__':
    main()
