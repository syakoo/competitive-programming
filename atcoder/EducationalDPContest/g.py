import sys

sys.setrecursionlimit(10**9)


def topological_sort(adjs: list, vn: int) -> list:
    result = []
    used = [0] * vn

    def dfs(vi: int):
        for vj in adjs[vi]:
            if used[vj]:
                continue
            used[vj] = 1
            dfs(vj)

        result.append(vi)

    for v_start in range(vn):
        if used[v_start]:
            continue

        dfs(v_start)

    return result[::-1]


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    XYs = [lmap(int, input().split()) for _ in range(m)]

    adjs = [[] for _ in range(n)]
    for x, y in XYs:
        adjs[x - 1].append(y - 1)

    verts = topological_sort(adjs, n)
    dp = [0] * n
    for vi in verts:
        for vj in adjs[vi]:
            dp[vj] = max(dp[vj], dp[vi] + 1)

    print(max(dp))


if __name__ == '__main__':
    main()
