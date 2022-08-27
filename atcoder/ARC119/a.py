import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    ans = 1 << 60
    for b in range(int(math.log2(n))+1):
        a, c = divmod(n, 1 << b)
        if c >= 0:
            ans = min(ans, a+b+c)

    print(ans)


if __name__ == '__main__':
    main()
