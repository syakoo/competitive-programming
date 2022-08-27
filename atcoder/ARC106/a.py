import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    for b in range(1, int(math.log(n, 5)) + 1):
        if n <= 5 ** b:
            continue
        a = math.log(n - 5**b, 3)
        a = int(a)
        if 3**a + 5 ** b == n:
            print(a, b)
            return
        if 3**(a-1) + 5 ** b == n:
            print(a - 1, b)
            return
        if 3**(a+1) + 5 ** b == n:
            print(a - 1, b)
            return

    print(-1)


if __name__ == '__main__':
    main()
