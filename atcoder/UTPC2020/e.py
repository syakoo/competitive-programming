
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    BHs = [0] * h
    BWs = [0] * w

    for hi in range(h):
        for wi in range(w):
            if Sss == '#':
                BHs[hi] += 1
                BWs[wi] += 1

    print(BHs, BWs)


if __name__ == '__main__':
    main()
