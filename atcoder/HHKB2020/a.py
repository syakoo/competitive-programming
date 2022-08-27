
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    t = input()

    if s == 'N':
        print(t)
        return

    print(t.upper())


if __name__ == '__main__':
    main()
