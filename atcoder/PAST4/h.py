
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, k = map(int, input().split())
    Sss = [lmap(int, input()) for _ in range(h)]

    for d in range(min(h, w), 0, -1):
        for hi in range(h - d + 1):
            for wi in range(w - d + 1):
                cnts = [0] * 10
                for dh in range(d):
                    for dw in range(d):
                        nh, nw = hi + dh, wi + dw
                        cnts[Sss[nh][nw]] += 1

                if d*d - max(cnts) <= k:
                    print(d)
                    return


if __name__ == '__main__':
    main()
