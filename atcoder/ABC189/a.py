
def lmap(func, iter):
    return list(map(func, iter))


def main():
    c = input()
    print(['Lost', 'Won'][int(c[0] == c[1] and c[1] == c[2])])


if __name__ == '__main__':
    main()
