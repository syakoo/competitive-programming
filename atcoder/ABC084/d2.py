import sys
from functools import lru_cache

sys.setrecursionlimit(10**9)


q = int(input())


@lru_cache(None)
def like_cnts(x: int) -> int:
    if x < 2:
        return 0
    if x == 2:
        return 0

    for y in range(2, int(x**(1/2)) + 1):
        if x % y == 0 or ((x+1)//2) % y == 0:
            return like_cnts(x-1)

    return like_cnts(x-1) + 1


for _ in range(q):
    l, r = map(int, input().split())
    print(like_cnts(r) - like_cnts(l-1))
