from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    """
    連結しているノードをまとめるだけ。答えはまとめた後のノードの数-1
    UnionFind も行けるが、BFS でやってみる
    """
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]

    # 連結リストに変換
    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a-1].append(b-1)
        adjs[b-1].append(a-1)

    # ノードの色分けをする
    colors = [-1]*n
    color = 0
    for vs in range(n):
        if colors[vs] >= 0:
            continue

        colors[vs] = color
        q = deque([vs])
        while q:
            vi = q.popleft()
            for vj in adjs[vi]:
                if colors[vj] >= 0:
                    continue
                colors[vj] = color
                q.append(vj)

        color += 1

    print(color-1)


if __name__ == '__main__':
    main()
