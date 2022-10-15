import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABCs = [sum(lmap(lambda x: 1 << (int(x) - 1), input().split()))
            for _ in range(m)]

    def bin_count(x: int):
        cnt = 0
        while x > 0:
            cnt += x % 2
            x //= 2

        return cnt

    ans = 0
    for x in range(1 << n):
        if any(map(lambda abc: abc & x == abc, ABCs)):
            continue

        y = 0
        for yi in filter(lambda x: bin_count(x) == 1, ((abc & x) ^ abc for abc in ABCs)):
            y |= yi

        ans = max(ans, bin_count(y))

    print(ans)


if __name__ == '__main__':
    main()
