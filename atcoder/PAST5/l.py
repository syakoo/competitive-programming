from functools import lru_cache
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    s = input()
    t = input()

    @lru_cache(None)
    def dfs(s: str) -> int:
        if len(s) < 3:
            return 0
        if t == s:
            return 1

        res = 0
        for l in range(len(s) - 2):
            if s[l:l+3] != t:
                continue
            cs = s[:l] + s[l+3:]
            res = max(res, dfs(cs) + 1)

        return res

    print(dfs(s))


if __name__ == '__main__':
    main()
