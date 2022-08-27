def lmap(func, iter):
    return list(map(func, iter))


def rotate(xss: list) -> list:
    h = len(xss)
    w = len(xss[0])

    result = [[0]*h for _ in range(w)]
    for hi in range(h):
        for wi in range(w):
            result[wi][h - hi - 1] = xss[hi][wi]

    return result


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    Tss = [input() for _ in range(h)]

    xss = [['#' for _ in range(w+21)] for _ in range(h+21)]
    for hi in range(h):
        for wi in range(w):
            xss[hi+10][wi+10] = Sss[hi][wi]

    def check(bh: int, bw: int, Tss: list) -> bool:
        for hi in range(len(Tss)):
            for wi in range(len(Tss[0])):
                if Tss[hi][wi] == xss[hi+bh][wi+bw] == '#':
                    return False

        return True

    for _ in range(4):
        Tss = rotate(Tss)
        for bh in range(len(xss)-len(Tss)):
            for bw in range(len(xss[0]) - len(Tss[0])):
                if check(bh, bw, Tss):
                    print('Yes')
                    return

    print('No')


if __name__ == '__main__':
    main()
