import math
import itertools


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m, x = map(int, input().split())
    CAs = [lmap(int, input().split()) for _ in range(n)]
    ans = math.inf

    for i in range(1, n+1):
        for CA_comb in itertools.combinations(CAs, i):
            values = [0 for _ in range(m + 1)]
            for CA in CA_comb:
                for vi, v in enumerate(CA):
                    values[vi] += v

            for vi in values[1:]:
                if vi < x:
                    break
            else:
                ans = min(ans, values[0])

    print(ans if ans != math.inf else -1)


if __name__ == '__main__':
    main()
