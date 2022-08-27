
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())

    for a in As:
        if a % 2 == 0:
            if a % 3 != 0 and a % 5 != 0:
                print('DENIED')
                return

    print('APPROVED')


if __name__ == '__main__':
    main()
