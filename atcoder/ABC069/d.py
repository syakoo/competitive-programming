def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    n = int(input())
    As = lmap(int, input().split())

    gridss = [[0]*w for _ in range(h)]
    cur = 0
    for hi in range(h):
        for wi in range(w):
            if hi % 2:
                wi = (- wi - 1) % w

            gridss[hi][wi] = cur + 1
            As[cur] -= 1

            if As[cur] == 0:
                cur += 1

    for row in gridss:
        print(*row)


if __name__ == '__main__':
    main()
