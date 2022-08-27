import math
from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)


@lru_cache(None)
def f(n: str, x: int):
    if x == 0:
        return 0
    if len(n) == 1:
        return min(x, int(n))

    res = int(n[:-1])+min(x, 9)
    if int(n[-1]) != 0:
        res += f(n[:-1], x//int(n[-1]))
    for a in range(1, 10):
        if a > int(n[-1]):
            res += f(str(int(n[:-1]) - 1), x//a)
        else:
            res += f(n[:-1], x//a)

    return res


def main():
    n, k = input().split()

    print(f(n, int(k)))


if __name__ == '__main__':
    main()
