import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    print(b - c)


if __name__ == '__main__':
    main()
