import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def argmin(xss: list) -> int:
    return min(range(len(xss)), key=lambda i: xss[i])


def main():
    n = int(input())
    Ss = lmap(int, input().split())
    Ts = lmap(int, input().split())

    i = argmin(Ts)
    for d in range(n):
        j = (i + d) % n
        Ts[(j+1) % n] = min(Ts[(j+1) % n], Ts[j] + Ss[j])

    print('\n'.join(map(str, Ts)))


if __name__ == '__main__':
    main()
