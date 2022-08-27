# 50 min

import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Css = [lmap(int, input().split()) for _ in range(n)]
    Ass = [[0 for _ in range(n)] for _ in range(n)]
    a1 = 0

    for i in range(1, n):
        for j in range(n):
            Ass[i][j] = Css[i][j] - Css[0][j]
            if j > 0 and Ass[i][j] != Ass[i][0]:
                print('No')
                return

        a1 = max(a1, -Ass[i][0])

    As = [Ass[i][0] + a1 for i in range(n)]
    Bs = [Css[0][i] - a1 for i in range(n)]

    print('Yes')
    print(*As)
    print(*Bs)


if __name__ == '__main__':
    main()
