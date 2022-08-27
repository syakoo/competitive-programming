
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    t = int(input())
    Cs = [int(input()) for _ in range(t)]

    for c in Cs:
        if c % 4 == 0:
            print('Even')
        elif c % 2 == 0:
            print('Same')
        else:
            print('Odd')


if __name__ == '__main__':
    main()
