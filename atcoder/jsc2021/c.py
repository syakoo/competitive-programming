
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())

    for x in range(b - a, 0, -1):
        x1, x2 = math.ceil(a / x)*x, (b // x)*x
        if a <= x1 <= b and a <= x2 <= b and x1 != x2:
            print(x)
            return


if __name__ == '__main__':
    main()
