
def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y = map(int, input().split())
    print(['No', 'Yes'][int(abs(x - y) <= 2)])


if __name__ == '__main__':
    main()

