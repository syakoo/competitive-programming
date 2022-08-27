def lmap(func, iter):
    return list(map(func, iter))


def main():
    s = input()
    t = input()
    print(["No", "Yes"][int(s == t[:-1])])


if __name__ == '__main__':
    main()
