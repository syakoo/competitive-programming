import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Cs = lmap(int, input().split())
    ABs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(n - 1)]
    di = set()
    anss = []

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a].append(b)
        adjs[b].append(a)

    def dfs(node: int, _from: int, di: set):
        if Cs[node] not in di:
            anss.append(node + 1)
            di = di.copy()
            di.add(Cs[node])

        for _to in adjs[node]:
            if _to == _from:
                continue
            dfs(_to, node, di)

    dfs(0, -1, di)
    anss.sort()
    print('\n'.join(str(ans) for ans in anss))


if __name__ == '__main__':
    main()
