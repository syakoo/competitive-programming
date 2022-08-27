import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    Cs = lmap(int, input().split())

    Xs = [0]*(n+1)
    Ys = [0]*(n+1)
    for a in As:
        Xs[a] += 1

    for c in Cs:
        Ys[Bs[c-1]] += 1

    ans = 0
    for x, y in zip(Xs, Ys):
        ans += x * y

    print(ans)


if __name__ == '__main__':
    main()
