
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = input()
    nn = len(n)

    if nn % 2 == 1:
        print(10**(nn//2) - 1)
        return

    a, b = int(n[:nn//2]), int(n[nn//2:])
    if a <= b:
        print(a)
        return
    else:
        print(a - 1)


if __name__ == '__main__':
    main()
