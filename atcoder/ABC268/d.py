import itertools
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    Ss = [input() for _ in range(n)]
    Ts = [input() for _ in range(m)]

    if n == 1 and len(Ss[0]) < 3:
        print(-1)
        return

    if n == 1:
        if Ss[0] in Ts:
            print(-1)
            return
        print(Ss[0])
        return

    values = []
    value_map = {'': 0}
    value_map_rev = ['']
    for s in Ss:
        if not s in value_map:
            value_map[s] = len(value_map)
            value_map_rev.append(s)

        values.append(value_map[s])

    valueSet = set()
    for t in Ts:
        flg = False
        v = 0
        for _t in t.split('_'):
            if not _t in value_map:
                flg = True
                break

            v = v * 10 + value_map[_t]

        if not flg:
            valueSet.add(v)

    for _ in range(17 - (sum(map(len, Ss)) + n-1)):
        for vs in itertools.permutations(values):
            if vs[0] == 0 or vs[-1] == 0:
                continue
            val = 0
            for v in vs:
                val = val*10 + v

            if val not in valueSet:
                print('_'.join(map(lambda v: value_map_rev[v], vs)))
                return

        values.append(0)

    print(-1)


if __name__ == '__main__':
    main()
