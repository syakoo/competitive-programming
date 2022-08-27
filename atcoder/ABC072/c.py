
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    cnts = [0] * (max(As) + 2)

    for a in As:
        if a - 1 > 0:
            cnts[a - 1] += 1
        cnts[a] += 1
        cnts[a + 1] += 1

    print(max(cnts))


if __name__ == '__main__':
    main()
