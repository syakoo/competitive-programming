
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    As = lmap(int, input().split())
    ass = filter(lambda a: a != x, As)
    print(' '.join(str(a) for a in ass))


if __name__ == '__main__':
    main()
