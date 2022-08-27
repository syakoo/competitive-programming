import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def pr_sets(s: set):
    l = list(s)
    l.sort()
    return ' '.join(map(str, l))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As = lmap(lambda x: (x[1] % 200, x[0] + 1), enumerate(As))

    idxss = [[] for _ in range(200)]
    for a, i in As:
        idxss[a].append(i)

    for idxs in idxss:
        if len(idxs) > 1:
            print('Yes')
            print(f'1 {idxs[0]}')
            print(f'1 {idxs[1]}')
            return

    set_idxs = [set() for _ in range(200)]
    for i, idxs in enumerate(idxss):
        if len(idxs) > 0:
            set_idxs[i].add(idxs[0])

    nidxss = set_idxs[:]
    for _ in range(200):
        next_idxss = [set() for _ in range(200)]
        for ai, nidxs in enumerate(nidxss):
            if len(nidxs) == 0:
                continue

            for aj, idxs in enumerate(set_idxs):
                if len(idxs) == 0 or nidxs.issuperset(idxs):
                    continue

                na = (ai + aj) % 200
                nsets = nidxs | idxs
                if len(nidxss[na]) > 0 and nidxss[na] != nsets:
                    print('Yes')
                    print(f'{len(nidxss[na])} {pr_sets(nidxss[na])}')
                    print(f'{len(nsets)} {pr_sets(nsets)}')
                    return
                elif len(next_idxss[na]) > 0 and next_idxss[na] != nsets:
                    print('Yes')
                    print(f'{len(next_idxss[na])} {pr_sets(next_idxss[na])}')
                    print(f'{len(nsets)} {pr_sets(nsets)}')
                    return
                next_idxss[na] = nsets

        for i, next_idxs in enumerate(next_idxss):
            nidxss[i] = next_idxs

    print('No')


if __name__ == '__main__':
    main()
