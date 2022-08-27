import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, q = map(int, input().split())
    UVs = [lmap(int, input().split()) for _ in range(m)]
    Cs = lmap(int, input().split())
    Ss = [lmap(int, input().split()) for _ in range(q)]

    adjs = [[] for _ in range(n)]
    for u, v in UVs:
        adjs[u - 1].append(v - 1)
        adjs[v - 1].append(u - 1)

    for s in Ss:
        if s[0] == 1:
            _, x = s
            print(Cs[x - 1])
            for vi in adjs[x - 1]:
                Cs[vi] = Cs[x - 1]
        else:
            _, x, y = s
            print(Cs[x - 1])
            Cs[x - 1] = y


if __name__ == '__main__':
    main()
