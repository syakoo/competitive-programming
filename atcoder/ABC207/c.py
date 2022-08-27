import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    TLRs = [lmap(int, input().split()) for _ in range(n)]

    LRs = []
    for t, l, r in TLRs:
        if t == 1:
            LRs.append((l, r))
        elif t == 2:
            LRs.append((l, r-0.1))
        elif t == 3:
            LRs.append((l+0.1, r))
        else:
            LRs.append((l+0.1, r-0.1))

    n = len(LRs)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            l1, r1 = LRs[i]
            l2, r2 = LRs[j]

            if l1 <= l2 <= min(r1, r2) or l2 <= l1 <= min(r1, r2):
                ans += 1

    print(ans)


if __name__ == '__main__':
    main()
