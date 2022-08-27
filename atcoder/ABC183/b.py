import math


def main():
    sx, sy, gx, gy = map(int, input().split())
    r = (sy + gy) / (sx - gx)
    b = sy - r*sx
    print(- b / r)


if __name__ == '__main__':
    main()
