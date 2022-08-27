
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    r, x, y = map(int, input().split())
    di = math.sqrt(x**2 + y**2)
    if di >= r:
        print(math.ceil(math.sqrt(x**2 + y**2)/r))
    else:
        print(2)


if __name__ == '__main__':
    main()
