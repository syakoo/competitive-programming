import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, n = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    ABIs = list((a, b, i) for i, (a, b) in enumerate(ABs))
    AABIs = sorted(ABIs, key=lambda ABI: ABI[0])
    BABIs = sorted(ABIs, key=lambda ABI: ABI[1])

    result = [[0, 0] for _ in range(n)]
    j = 1
    for k, (a, b, i) in enumerate(AABIs):
        result[i][0] = j
        if k != n-1 and AABIs[k+1][0] != a:
            j += 1
    j = 1
    for k, (a, b, i) in enumerate(BABIs):
        result[i][1] = j
        if k != n-1 and BABIs[k+1][1] != b:
            j += 1

    print('\n'.join(f'{a} {b}' for a, b in result))


if __name__ == '__main__':
    main()
