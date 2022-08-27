from itertools import combinations
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, x = map(int, input().split())
    As = lmap(int, input().split())
    anss = []

    for i in range(1, n+1):
        x_i = x % i
        for As_i in combinations(As, i):
            s_As = sum(As_i)
            if s_As % i == x_i:
                anss.append((i, s_As))

    ans = math.inf
    for l, sumA in anss:
        ans = min(ans, (x-sumA) // l)

    print(ans)


if __name__ == '__main__':
    main()
