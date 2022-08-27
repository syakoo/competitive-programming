
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    x = input()
    print(x.split('.')[0])


if __name__ == '__main__':
    main()
