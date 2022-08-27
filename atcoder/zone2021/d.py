import math
from itertools import combinations
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABCDEs = [lmap(int, input().split()) for _ in range(n)]
    mxs = [10**9] * n
    for abs in ABCDEs:
        for i, a in enumerate(abs):
            mxs[i] = min(mxs[i], a)

    mni = mxs.index(min(mxs))

    ABCDEs.sort(key=lambda x: x[mni], reverse=True)
    ans = 0
    for i in range(int(n**(1/2))):
        minmax = 0
        for j, k in combinations([l for l in range(n) if i != l], r=2):
            mxs = ABCDEs[0]
            for mxi in range(5):
                mxs[mxi] = max(mxs[mxi], ABCDEs[j][mxi], ABCDEs[k][mxi])
            minmax = max(minmax, min(mxs))

        ans = max(ans, minmax)

    print(ans)

if __name__ == '__main__':
    main()
