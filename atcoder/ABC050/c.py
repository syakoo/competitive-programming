# 6 min
from collections import Counter


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    Acnts = Counter(As)

    if n % 2 == 1:
        if Acnts[0] != 1:
            print(0)
            return

    for i in range(n % 2+1, n, 2):
        if Acnts[i] != 2:
            print(0)
            return

    print(pow(2, (n//2), 10**9 + 7))


if __name__ == '__main__':
    main()
