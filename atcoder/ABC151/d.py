# 13 min
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    HWs = [input() for _ in range(h)]
    ans = 0

    for hs in range(h):
        for ws in range(w):
            if HWs[hs][ws] == '#':
                continue

            flgs = [[False for _ in range(w)] for _ in range(h)]
            flgs[hs][ws] = True
            q = [(hs, ws)]
            turn = 0
            while q:
                n_q = []
                turn += 1
                for hi, wi in q:
                    for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                        hj, wj = hi + dh, wi + dw

                        if 0 <= hj < h and 0 <= wj < w and HWs[hj][wj] == '.' and flgs[hj][wj] == False:
                            flgs[hj][wj] = True
                            n_q.append((hj, wj))

                q = n_q

            ans = max(ans, turn - 1)

    print(ans)


if __name__ == '__main__':
    main()
