import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())
    
    if a == 0:
        print('Silver')
    elif b == 0:
        print('Gold')
    else:
        print('Alloy')


if __name__ == '__main__':
    main()
