import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    for a in range(1, 38):
        for b in range(1, 26):
            if 3 ** a + 5 ** b == n:
                print(a, b)
                return
    print(-1)


if __name__ == '__main__':
    main()
