
def lmap(func, iter):
    return list(map(func, iter))


def main():
    m, h = map(int, input().split())
    print(['Yes', 'No'][int(h % m > 0)])


if __name__ == '__main__':
    main()
