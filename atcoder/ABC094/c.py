from statistics import median_low, median_high


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Xs = lmap(int, input().split())

    l, r = median_low(Xs), median_high(Xs)
    for x in Xs:
        if l >= x:
            print(r)
        else:
            print(l)


if __name__ == '__main__':
    main()
