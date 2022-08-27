# 45 min
from functools import reduce
import math


def lmap(func, iter):
    return list(map(func, iter))


def even_cnt(x: int) -> int:
    cnt = 0
    for i in range(50):
        if x >> i & 1:
            return cnt

        cnt += 1


def main():
    n, m = map(int, input().split())
    As = lmap(int, input().split())

    even_cnts = sorted(map(even_cnt, As))
    if not (even_cnts and even_cnts[0] == even_cnts[-1]):
        print(0)
        return

    mn = reduce(lambda p, x: (p*x)//math.gcd(p, x), As, 1) // 2
    print((m//mn+1)//2)


if __name__ == '__main__':
    main()
