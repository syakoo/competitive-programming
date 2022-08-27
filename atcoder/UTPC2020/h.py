
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]
    BHs = [0] * h
    BWs = [0] * w

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                BHs[hi] += 1
                BWs[wi] += 1
    Brow_cnts = [0] * (w + 1)
    Bcol_cnts = [0] * (h + 1)
    for bh in BHs:
        Brow_cnts[bh] += 1
    for bw in BWs:
        Bcol_cnts[bw] += 1

    cw, cb = 0, h
    rw, rb = 0, w
    print(Brow_cnts)
    f = [True]*4
    i = 0

    while i < h * w and cw < cb and rw < rb:
        # black
        if f[0] and Bcol_cnts[cb]:
            rw += Bcol_cnts[cb]
            f[0] = True
        else:
            f[0] = False
        cw += Brow_cnts[rb]

        # white
        rb -= Bcol_cnts[cw]
        cb -= Brow_cnts[rw]
        i += 1

    if cw >= cb or rw >= rb:
        print(max(h, w))
    else:
        print(cw + rw + (h - cb) + (w - rb))


if __name__ == '__main__':
    main()
