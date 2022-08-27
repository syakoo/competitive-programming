import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As.sort()

    pos_idx = n - 1
    for i, a in enumerate(As):
        if a >= 0:
            pos_idx = i
            break
    if pos_idx == 0:
        pos_idx = 1

    queries = []
    Bs = As[:pos_idx]
    a0 = As[0]
    for i in range(pos_idx, n-1):
        queries.append((Bs[0], As[i]))
        Bs[0] -= As[i]

    ans = As[-1]
    for b in Bs:
        queries.append((ans, b))
        ans -= b

    print(ans)
    print('\n'.join(f'{q[0]} {q[1]}' for q in queries))


if __name__ == '__main__':
    main()
