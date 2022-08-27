# 15 min

import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    CSFs = [lmap(int, input().split()) for _ in range(n - 1)]
    times = [0] * n

    for i in range(n - 1):
        for j in range(i):
            if times[j] <= CSFs[i][1]:
                times[j] = CSFs[i][1] + CSFs[i][0]
            else:
                t = math.ceil((times[j] - CSFs[i][1]) / CSFs[i][2])
                times[j] = CSFs[i][1] + CSFs[i][0] + CSFs[i][2] * t

        times[i] = CSFs[i][0] + CSFs[i][1]

    print('\n'.join(map(str, times)))


if __name__ == '__main__':
    main()
