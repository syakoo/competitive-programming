
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    print(s[::2])


if __name__ == '__main__':
    main()
