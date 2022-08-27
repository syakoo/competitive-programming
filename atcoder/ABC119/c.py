# 10 min
from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, a, b, c = map(int, input().split())
    Ls = [int(input()) for _ in range(n)]

    ans = float('inf')
    for pats in product(range(4), repeat=n):
        if not pats.count(1) or not pats.count(2) or not pats.count(3):
            continue
        bams = [0]*3
        for i, pat in enumerate(pats):
            if pat > 0:
                bams[pat-1] += Ls[i]

        res = (pats.count(1) + pats.count(2) + pats.count(3) - 3) * 10
        for bam, exp in zip(bams, (a, b, c)):
            res += abs(bam - exp)

        ans = min(ans, res)

    print(ans)


if __name__ == '__main__':
    main()
