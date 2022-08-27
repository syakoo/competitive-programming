
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    PYs = [lmap(int, input().split()) for _ in range(m)]

    prev_p = 0
    PYs.sort(key=lambda x: x[1])
    PYs.sort(key=lambda x: x[0])



if __name__ == '__main__':
    main()
