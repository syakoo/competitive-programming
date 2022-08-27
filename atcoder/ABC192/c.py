
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    ans = n

    for _ in range(k):
        ans = f(ans)

    print(ans)


def f(x: int):
    x_str = list(str(x))
    x_str.sort()
    g1 = int(''.join(x_str[::-1]))
    g2 = int(''.join(x_str))
    return g1 - g2


if __name__ == '__main__':
    main()
