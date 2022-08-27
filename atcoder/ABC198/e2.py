import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Cs = lmap(int, input().split())
    ABs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(n - 1)]

    adjs = [[] for _ in range(n)]
    for a, b in ABs:
        adjs[a].append(b)
        adjs[b].append(a)

    anss = []
    cnts = [0]*(max(Cs) + 1)

    def dfs(node: int, _from: int):
        if cnts[Cs[node]] == 0:
            anss.append(node + 1)
        cnts[Cs[node]] += 1

        for _to in adjs[node]:
            if _to == _from:
                continue
            dfs(_to, node)

        cnts[Cs[node]] -= 1

    dfs(0, -1)
    anss.sort()
    print('\n'.join(str(ans) for ans in anss))


if __name__ == '__main__':
    main()
