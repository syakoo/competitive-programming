# 19 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s1 = input()
    s2 = input()
    MOD = 10**9 + 7

    ms = []
    cur = 0
    while cur < n:
        if s1[cur] == s2[cur]:
            ms.append(1)
            cur += 1
        else:
            ms.append(0)
            cur += 2

    ans = 3 if ms[0] else 6
    for mi in range(1, len(ms)):
        if ms[mi]:
            if ms[mi-1]:
                ans *= 2
        else:
            if ms[mi-1]:
                ans *= 2
            else:
                ans *= 3
        ans %= MOD

    print(ans)


if __name__ == '__main__':
    main()
