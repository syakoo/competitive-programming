
def lmap(func, iter):
    return list(map(func, iter))


def main():
    w, h, x, y = map(int, input().split())
    print((w * h)/2, int((x, y) == (w/2, h/2)))


if __name__ == '__main__':
    main()
