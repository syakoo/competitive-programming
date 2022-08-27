import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = input()
    As = lmap(int, input().split())

    k = min(abs(As[i] - As[i+1]) for i in range(n))
    print(k)
    for i in range(k):
        print(*map(lambda a: (a + i)//k, As))


if __name__ == '__main__':
    main()
