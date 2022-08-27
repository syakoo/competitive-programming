
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    xs = lmap(int, input().split())
    ave = round(sum(xs) / n)

    print(sum(map(lambda x: (x-ave)**2, xs)))


if __name__ == '__main__':
    main()
