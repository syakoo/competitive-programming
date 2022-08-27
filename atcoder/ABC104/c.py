import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    d, g = map(int, input().split())
    PCs = [lmap(int, input().split()) for _ in range(d)]

    cnts = {0: 0}
    for j, (p, c) in enumerate(PCs):
        new_cnts = {}
        for i in range(p):
            for k, v in cnts.items():
                nk = k + 100*(i + 1)*(j + 1)
                if i == p - 1:
                    nk += c
                if nk in new_cnts:
                    new_cnts[nk] = min(new_cnts[nk], v+i+1)
                else:
                    new_cnts[nk] = v+i+1

        for k, v in new_cnts.items():
            if k in cnts:
                cnts[k] = min(cnts[k], v)
            else:
                cnts[k] = v

    ans = 1 << 60
    for k, v in cnts.items():
        if k >= g:
            ans = min(ans, v)

    print(ans)


if __name__ == '__main__':
    main()
