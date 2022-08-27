
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    print(s[1:] + s[0])


if __name__ == '__main__':
    main()
