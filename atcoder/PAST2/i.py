
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    idxs = list(range(1 << n))
    anss = [0]*(1 << n)

    for i in range(n - 1):
        nexts = []
        for j in range(0, len(idxs), 2):
            ax = idxs[j]
            ay = idxs[j + 1]
            if As[ax] > As[ay]:
                nexts.append(ax)
                anss[ay] = i + 1
            else:
                nexts.append(ay)
                anss[ax] = i + 1

        idxs = nexts

    anss[idxs[0]] = n
    anss[idxs[1]] = n

    print('\n'.join(str(a) for a in anss))


if __name__ == '__main__':
    main()
