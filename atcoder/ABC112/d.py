
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())

    for i in range(m//n, -1, -1):
        if m % i == 0:
            print(i)
            return


if __name__ == '__main__':
    main()
