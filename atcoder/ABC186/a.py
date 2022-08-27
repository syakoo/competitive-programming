
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, w = map(int, input().split())
    print(n // w)


if __name__ == '__main__':
    main()

