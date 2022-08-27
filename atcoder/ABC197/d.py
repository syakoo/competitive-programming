
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    x0, y0 = map(int, input().split())
    x1, y1 = map(int, input().split())
    xo, yo = (x0 + x1) / 2, (y0 + y1) / 2

    dx, dy = x0 - xo, y0 - yo
    theta = math.radians(360 / n)
    print(dx*math.cos(theta) - dy*math.sin(theta) + xo,
          dx*math.sin(theta) + dy*math.cos(theta) + yo)


if __name__ == '__main__':
    main()
