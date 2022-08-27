
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    patt = 0

    if k % 2 == 0:
        patt = n // (k // 2) - (n//k)

    print(patt**3 + (n//k)**3)


if __name__ == '__main__':
    main()
