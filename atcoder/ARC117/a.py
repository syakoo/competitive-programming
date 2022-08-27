
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())
    As = list(range(1, a + 1))
    Bs = list(range(-1, -b - 1, -1))

    if a > b:
        Bs[-1] = Bs[-1] - (a*(a+1)//2 - b*(b+1)//2)
    else:
        As[-1] = As[-1] + b*(b+1)//2 - a*(a+1)//2

    print(*As, *Bs)


if __name__ == '__main__':
    main()
