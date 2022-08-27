
def lmap(func, iter):
    return list(map(func, iter))


def main():
    v, t, s, d = map(int, input().split())
    if t*v <= d <= v*s:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
