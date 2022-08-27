
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    VPs = [lmap(int, input().split()) for _ in range(n)]
    a = 0

    for i, (v, p) in enumerate(VPs):
        a += v * p
        if a > x*100:
            print(i + 1)
            return

    print(-1)


if __name__ == '__main__':
    main()
