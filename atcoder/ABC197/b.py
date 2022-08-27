
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, x, y = map(int, input().split())
    Sss = [input() for _ in range(h)]
    ans = 0
    x -= 1
    y -= 1

    for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nh, nw = x + dh, y + dw

        while 0 <= nh < h and 0 <= nw < w and Sss[nh][nw] == '.':
            ans += 1
            nh += dh
            nw += dw

    print(ans + 1)


if __name__ == '__main__':
    main()
