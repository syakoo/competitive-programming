# 15 min
from itertools import permutations


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, c = map(int, input().split())
    Dcs = [lmap(int, input().split()) for _ in range(c)]
    Cs = [lmap(lambda x: int(x) - 1, input().split()) for _ in range(n)]

    if n == 1:
        print(0)
        return

    cntss = [[0]*c for _ in range(3)]
    for h in range(n):
        for w in range(n):
            cntss[(h + w) % 3][Cs[h][w]] += 1

    ans = float('inf')
    for colors in permutations(range(c), r=3):
        res = 0
        for i, coli in enumerate(colors):
            for colj, cnt in enumerate(cntss[i]):
                res += Dcs[colj][coli] * cnt

        ans = min(ans, res)

    print(ans)


if __name__ == '__main__':
    main()
