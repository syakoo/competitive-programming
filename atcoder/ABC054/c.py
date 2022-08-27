import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a - 1].append(b - 1)
        adjs[b - 1].append(a - 1)

    used = [0]*n
    used[0] = 1

    def dfs(vi: int) -> int:
        if all(used):
            return 1

        cnt = 0
        for vj in adjs[vi]:
            if not used[vj]:
                used[vj] = 1
                cnt += dfs(vj)
                used[vj] = 0

        return cnt

    ans = dfs(0)
    print(ans)


if __name__ == '__main__':
    main()
