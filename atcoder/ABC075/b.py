from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    ans = [[0] * w for _ in range(h)]

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                ans[hi][wi] = '#'
                continue

            for dh, dw in product((-1, 0, 1), repeat=2):
                if dh == dw == 0:
                    continue
                nh, nw = hi + dh, wi + dw

                if 0 <= nh < h and 0 <= nw < w and Sss[nh][nw] == '#':
                    ans[hi][wi] += 1

    for hi in range(h):
        print(''.join(map(str, ans[hi])))


if __name__ == '__main__':
    main()
