
import math
from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w = map(int, input().split())
    Cs = lmap(lambda x: int(x) - 1, input().split())
    Ds = lmap(lambda x: int(x) - 1, input().split())
    Sss = [input() for _ in range(h)]
    Wss = [[-1 for _ in range(w)] for _ in range(h)]

    q = deque([Cs])
    nq = deque([])
    loop = 0

    while q:
        while q:
            ph, pw = q.popleft()

            if Wss[ph][pw] != -1:
                continue

            Wss[ph][pw] = loop
            for dh in range(-2, 3):
                for dw in range(-2, 3):
                    nh, nw = ph + dh, pw + dw
                    if nh < 0 or nh >= h or nw < 0 or nw >= w or Sss[nh][nw] == '#':
                        continue

                    if dh*dw == 0 and abs(dh + dw) <= 1:
                        q.append((nh, nw))
                    else:
                        nq.append((nh, nw))

        q = nq
        nq = deque([])
        loop += 1

    print(Wss[Ds[0]][Ds[1]])


if __name__ == '__main__':
    main()
