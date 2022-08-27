import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n-1)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a-1].append(b-1)
        adjs[b-1].append(a-1)

    adjs = lmap(sorted, adjs)
    result = []
    used = [0]*n
    used[0] = 1

    def dfs(vi: int):
        result.append(vi + 1)

        for vj in adjs[vi]:
            if used[vj] == 0:
                used[vj] = 1
                flg = dfs(vj)
                result.append(vi + 1)
                if flg:
                    return True

        if vi == 0:
            return True
        return False

    dfs(0)
    print(*result)


if __name__ == '__main__':
    main()
