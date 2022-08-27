from functools import reduce
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def rotate(xss: list) -> list:
    n = len(xss)
    result = [[] for _ in range(n)]
    for hi in range(n):
        for wi in range(n):
            result[hi][wi] = xss[wi][n-hi-1]

    return result


def main():
    n = int(input())
    k = int(input())
    Sss = [input() for _ in range(n)]
    h = n + 2*k
    w = n + 4*k
    boards = [[0]*(w) for _ in range(h)]

    for hi in range(n):
        for wi in range(n):
            boards[hi+k][wi+k] = 1 if Sss[hi][wi] == '.' else 0

    minos = set()
    bss = [[0]*k for _ in range(2*k)]
    q = []

    def dfs(pos: list, depth: int):
        if depth == k:
            minos.add(reduce(lambda prev, cur: prev +
                             (1 << (cur[0]+cur[1]*n)), q + [pos], 0))
            return

        q.append(pos)
        hi, wi = pos
        bss[hi][wi] = 1
        for hi, wi in q:
            for nh, nw in [(hi, wi+1), (hi+1, wi), (hi-1, wi)]:
                if bss[nh][nw] == 0:
                    dfs((nh, nw), depth+1)

        q.pop()
        bss[hi][wi] = 0

    dfs((k, 0), 1)

    def check() -> int:
        cnt = 0
        for hi in range(h - 2*k):
            for wi in range(w - k):
                bit = 0
                for dh in range(2*k):
                    for dw in range(k):
                        if boards[hi+dh][wi+dw]:
                            bit += (1 << (dh + (dw*n)))
                for mino in minos:
                    if bit & mino == mino:
                        cnt += 1
        return cnt

    print(check())


if __name__ == '__main__':
    main()
