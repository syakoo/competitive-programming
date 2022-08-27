
def lmap(func, iter):
    return list(map(func, iter))


def main():
    x = int(input())
    print(100 - (x % 100))


if __name__ == '__main__':
    main()
