
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Ds = input().split()

    for i in range(n, 10**6):
        flg = True
        for d in Ds:
            if str(i).count(d) > 0:
                flg = False
                break

        if flg:
            print(i)
            return


if __name__ == '__main__':
    main()
