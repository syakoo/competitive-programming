
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Sss = [list(input()) for _ in range(n)]

    for j in range(n - 1, 0, -1):
        for i in range(2*n - 1):
            if Sss[j][i] != 'X':
                continue

            for k in range(max(0, i-1), min(2*n - 2, i+2)):
                if Sss[j - 1][k] == '#':
                    Sss[j - 1][k] = 'X'

    print('\n'.join(''.join(ss) for ss in Sss))


if __name__ == '__main__':
    main()
