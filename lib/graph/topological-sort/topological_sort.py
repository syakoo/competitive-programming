import sys

sys.setrecursionlimit(10**9)


def topological_sort(adjs: list, vn: int) -> list:
    """トポロジカルソート(syakoo🐍) Θ(|V|+|E|)
    ※ 再帰の上限を変えること(sys.setrecursionlimit)

    Args:
        adjs (list): 隣接リスト
        vn (int): 頂点数

    Returns:
        list: ソート後の頂点のリスト
    """
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
