
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y, z = map(int, input().split())
    print(math.ceil(y/x * z) - 1)


if __name__ == '__main__':
    main()
