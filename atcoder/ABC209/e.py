import sys
from collections import defaultdict
sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ss = [input() for _ in range(n)]

    lasts = defaultdict(list)
    firsts = defaultdict(list)
    for i, s in enumerate(ss):
        lasts[s[-3:]].append(i)
        firsts[s[:3]].append(i)

    adjs = [[] for _ in range(n)]
    for k, v in lasts.items():
        for vi in v:
            adjs[vi] = firsts[k]

    wins = [[-2, -2] for _ in range(n)]

    def dfs(v: int) -> tuple:
        # 0 lose, 1 win, 2 draw
        if not adjs[v]:
            wins[v] = [1, 0]
            return 1, 0

        wins[v] = [-1, -1]
        loop = False
        u = 0
        for vi in adjs[v]:
            if wins[vi][0] == 1:
                wins[v][1] = 1
            if wins[vi][1] == 1:
                wins[v][0] = 1
            if wins[vi][1] == -1 or wins[vi][1] == 2:
                loop = True
            if wins[vi][0] == -1 or wins[vi][0] == 2:
                loop = True

            if wins[vi][0] == -2:
                res = dfs(vi)
                if res[0] == 1:
                    wins[v][1] = 1
                elif res[0] == 2 or res[1] == 2:
                    loop = True
                if res[1] == 1:
                    wins[v][0] = 1

        if loop:
            if wins[v][0] != 1:
                wins[v][0] = 2
            if wins[v][1] != 1:
                wins[v][1] = 2

        if wins[v][0] == -1:
            wins[v][0] = 0
        if wins[v][1] == -1:
            wins[v][1] = 0

        return wins[v]

    for i in range(n):
        if wins[i][0] != -2:
            continue
        dfs(i)

    for f, t in wins:
        if f == 1:
            print('Takahashi')
        elif f == 0:
            print('Aoki')
        else:
            print('Draw')


if __name__ == '__main__':
    main()
