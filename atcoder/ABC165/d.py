# 25 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    a, b, n = map(int, input().split())
    print((a*(min(n, b - 1)))//b)


if __name__ == '__main__':
    main()
