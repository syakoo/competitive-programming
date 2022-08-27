import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    As.sort()
    Bs.sort()

    bi = 0
    ans = 1 << 60
    for a in As:
        while bi < m and Bs[bi] < a:
            ans = min(ans, abs(Bs[bi] - a))
            bi += 1

        if bi < m:
            ans = min(ans, abs(Bs[bi] - a))
    
    print(ans)


if __name__ == '__main__':
    main()
