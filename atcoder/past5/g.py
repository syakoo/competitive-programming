import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Sss = [input() for _ in range(h)]

    all_cnt = sum(Ss.count('#') for Ss in Sss)

    stack = []
    visited = set()

    def dfs(hi: int, wi: int):
        stack.append((hi, wi))
        visited.add((hi, wi))
        if all_cnt == len(visited):
            return stack

        for dh, dw in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= hi + dh < h and 0 <= wi + dw < w:
                if Sss[hi + dh][wi + dw] == '#' and (hi + dh, wi + dw) not in visited:
                    res = dfs(hi + dh, wi + dw)

                    if res:
                        return res

        stack.pop()
        visited.remove((hi, wi))

    for hi in range(h):
        for wi in range(w):
            if Sss[hi][wi] == '#':
                res = dfs(hi, wi)

                if res:
                    print(all_cnt)
                    print('\n'.join(f'{t[0] + 1} {t[1] + 1}' for t in res))
                    return


if __name__ == '__main__':
    main()
