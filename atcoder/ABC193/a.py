
def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b = map(int, input().split())
    print(((a - b) / a) * 100)


if __name__ == '__main__':
    main()
