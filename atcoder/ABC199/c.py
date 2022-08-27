
import math
import sys

sys.setrecursionlimit(10**6)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = list(input())
    q = int(input())
    TABs = [lmap(int, input().split()) for _ in range(q)]
    s1, s2 = s[:n], s[n:]

    for t, a, b in TABs:
        if t == 2:
            s2, s1 = s1, s2
        else:
            a -= 1
            b -= 1
            if a < n and b < n:
                s1[a], s1[b] = s1[b], s1[a]
            elif a < n and b >= n:
                s1[a], s2[b % n] = s2[b % n], s1[a]
            else:
                s2[a % n], s2[b % n] = s2[b % n], s2[a % n]

    print(''.join([''.join(s1), ''.join(s2)]))


if __name__ == '__main__':
    main()
