import networkx as nx
import itertools as it


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, r = map(int, input().split())
    Rs = lmap(int, input().split())
    ABCs = [lmap(int, input().split()) for _ in range(m)]

    G = nx.Graph()
    G.add_weighted_edges_from(ABCs)
    dists = nx.floyd_warshall(G)

    ans = float("inf")
    for rs in it.permutations(Rs):
        res = 0
        for i in range(1, len(rs)):
            res += dists[rs[i-1]][rs[i]]

        ans = min(ans, res)

    print(ans)


if __name__ == '__main__':
    main()
