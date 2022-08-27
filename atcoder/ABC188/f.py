
def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y = map(int, input().split())

    if y <= x:
        print(x - y)
        return
    q = (y // x)
    if q % 2 == 0:
        r = y % x


if __name__ == '__main__':
    main()
