import sys

sys.setrecursionlimit(10**6)


def reverse_adjs(vn: int, adjs: list) -> list:
    """有向辺を逆にする O(|E|)

    Args:
        vn (int): ノード数 |V|
        adjs (list): 連結リスト

    Returns:
        list: 逆にした有向辺
    """
    result = [[] for _ in range(vn)]

    for vi in range(vn):
        for vj in adjs[vi]:
            result[vj].append(vi)

    return result


def scc(vn: int, adjs: list, radjs: list = None) -> list:
    """強連結成分分解(SCC)を求める🐍。O(|V| + |E|)

    Args:
        vn (int): ノード数 |V|
        adjs (list): 連結リスト
        radjs (list, optional): 反転した連結リスト. Defaults to None.

    Returns:
        list: 強連結成分のグループのリスト
    """
    if radjs is None:
        radjs = reverse_adjs(vn, adjs)

    visited = [0]*vn
    vs = []

    def dfs(v: int):
        for vi in adjs[v]:
            if visited[vi]:
                continue

            visited[vi] = 1
            dfs(vi)

        vs.append(v)

    sc = []

    def rdfs(v: int):
        sc.append(v)
        for vi in radjs[v]:
            if visited[vi]:
                continue

            visited[vi] = 1
            rdfs(vi)

    for vi in range(vn):
        if visited[vi]:
            continue

        visited[vi] = 1
        dfs(vi)

    visited = [0] * vn
    result = []
    for vi in reversed(vs):
        if visited[vi]:
            continue

        visited[vi] = 1
        sc = []
        rdfs(vi)
        result.append(sc)

    return result


if __name__ == '__main__':
    vn = 4
    adjs = [[1, 2, 3], [], [2], [0, 1]]
    print(reverse_adjs(vn, adjs))  # [[3], [0, 3], [0, 2], [0]]

    vn = 9
    adjs = [[1], [6], [7], [1, 5], [3], [7, 8], [0], [2], [4]]
    print(scc(vn, adjs))
