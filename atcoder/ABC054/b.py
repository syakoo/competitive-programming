import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def same(ns: tuple, m: int, Ass: list, Bss: list) -> bool:
    ni, nj = ns
    for mi in range(m):
        for mj in range(m):
            if Ass[ni + mi][nj + mj] != Bss[mi][mj]:
                return False

    return True


def main():
    n, m = map(int, input().split())
    Ass = [input() for _ in range(n)]
    Bss = [input() for _ in range(m)]

    for ni in range(n - m + 1):
        for nj in range(n - m + 1):
            if same((ni, nj), m, Ass, Bss):
                print('Yes')
                return

    print('No')


if __name__ == '__main__':
    main()
