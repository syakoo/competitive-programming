
def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, c = map(int, input().split())

    if c == 0:
        if a <= b:
            print("Aoki")
        else:
            print("Takahashi")
    else:
        if b <= a:
            print("Takahashi")
        else:
            print("Aoki")


if __name__ == '__main__':
    main()
