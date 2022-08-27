import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ACs = [lmap(int, input().split()) for _ in range(m)]

    GCDs = dict()
    for a, c in ACs:
        gcd = math.gcd(a, n)
        if gcd in GCDs:
            GCDs[gcd] = min(GCDs[gcd], c)
        else:
            GCDs[gcd] = c

    ACs = sorted(GCDs.items(), key=lambda x: x[1])
    if ACs[0][0] == 1:
        print((n-1)*ACs[0][1])
    elif len(ACs) == 1:
        print(-1)
    else:
        ans = 1 << 60
        nn = len(ACs)
        for i in range(nn-1):
            a1, c1 = ACs[i]
            for j in range(i+1, nn):
                a2, c2 = ACs[j]
                if min(a1, a2) == 1 or max(a1, a2) % min(a1, a2):
                    ans = min(ans, (n-a1)*c1 + (a1-1)*c2)
        print(ans)


if __name__ == '__main__':
    main()
