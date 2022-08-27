
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    print(pow(10, n, m*m) // m % m)


if __name__ == '__main__':
    main()
