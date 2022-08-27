import math
import sys
from itertools import combinations
from collections import deque
from functools import reduce

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    k = int(input())
    Sss = [input() for _ in range(n)]

    whites = []
    for hi in range(n):
        for wi in range(n):
            if Sss[hi][wi] == '.':
                whites.append((hi, wi))

    ans = set()
    used = [[0]*n for _ in range(n)]
    stack = []

    def dfs(pos: list, depth: int):
        if depth == k:
            ans.add(reduce(lambda prev, cur: prev +
                    (1 << (cur[0]+cur[1]*n)), stack + [pos], 0))
            return

        stack.append(pos)
        hi, wi = pos
        used[hi][wi] = 1
        for hi, wi in stack:
            for nh, nw in [(hi, wi+1), (hi+1, wi), (hi-1, wi)]:
                if 0 <= nh < n and 0 <= nw < n and used[nh][nw] == 0 and Sss[nh][nw] == '.':
                    dfs((nh, nw), depth+1)

        stack.pop()
        used[hi][wi] = 0

    for hi, wi in whites:
        dfs((hi, wi), 1)

    print(len(ans))


if __name__ == '__main__':
    main()
