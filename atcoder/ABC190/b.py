
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, s, d = map(int, input().split())
    XYs = [lmap(int, input().split()) for _ in range(n)]

    for x, y in XYs:
        if x < s and y > d:
            print("Yes")
            return

    print("No")


if __name__ == '__main__':
    main()
