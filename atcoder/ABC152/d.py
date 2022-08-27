# 10 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())

    cntss = [[0]*10 for _ in range(10)]
    for x in range(1, n+1):
        x_str = str(x)
        cntss[int(x_str[0])][int(x_str[-1])] += 1

    ans = 0
    for i in range(1, 10):
        for j in range(1, 10):
            ans += cntss[i][j] * cntss[j][i]

    print(ans)


if __name__ == '__main__':
    main()
