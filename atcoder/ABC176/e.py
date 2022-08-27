
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, m = map(int, input().split())
    HWs = [lmap(int, input().split()) for _ in range(m)]
    Mset = set()
    Mhs = [0 for _ in range(h)]
    Mws = [0 for _ in range(w)]

    for hi, wi in HWs:
        Mset.add((hi - 1, wi - 1))
        Mhs[hi - 1] += 1
        Mws[wi - 1] += 1

    hmax = max(Mhs)
    wmax = max(Mws)
    hargmaxes = [i for i, h in enumerate(Mhs) if h == hmax]
    wargmaxes = [i for i, w in enumerate(Mws) if w == wmax]

    if len(hargmaxes)*len(wargmaxes) > m:
        print(hmax + wmax)
        return

    for hi in hargmaxes:
        for wi in wargmaxes:
            if (hi, wi) not in Mset:
                print(hmax + wmax)
                return

    print(hmax + wmax - 1)


if __name__ == '__main__':
    main()
