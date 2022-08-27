
def lmap(func, iter):
    return list(map(func, iter))


def main():
    Xs = lmap(int, input().split())
    Xs.sort(reverse=True)
    print(Xs[2])


if __name__ == '__main__':
    main()
