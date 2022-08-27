import math


def lmap(func, iter):
    return list(map(func, iter))


def check(x, di, m):
    a = 0
    x_len = len(x)
    for i, xi in enumerate(x):
        a += int(xi)*(di**(x_len - i - 1))
        if a > m:
            return False

    return True


def main():
    x = input()
    x_len = len(x)
    m = int(input())
    d = max(map(lambda c: int(c), x))

    if x_len == 1:
        if (int(x) > m):
            print(0)
        else:
            print(1)
        return
    k = (m / int(x[0])) ** (1/(x_len-1))
    k = math.floor(k)

    for di in range(k, d, -1):
        if (check(x, di, m)):
            print(max(0, di - d))
            return

    print(0)


if __name__ == '__main__':
    main()
