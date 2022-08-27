# 19 min

from collections import deque


def lmap(func, iter):
    return list(map(func, iter))


def solve(Ass, bs):
    fss = [[0 for _ in range(10)] for _ in range(10)]
    times = 0
    for hi in range(10):
        for wi in range(10):
            if Ass[hi][wi] != 'o' or fss[hi][wi] == 1:
                continue

            if times >= 1:
                return False

            times += 1
            q = deque([(hi, wi)])
            while q:
                hn, wn = q.popleft()

                for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                    hm, wm = hn + dh, wn + dw

                    if 0 <= hm < 10 and 0 <= wm < 10 and fss[hm][wm] == 0:
                        if Ass[hm][wm] == 'o' or (hm, wm) == bs:
                            fss[hm][wm] = 1
                            q.append((hm, wm))

    return True


def main():
    Ass = [input() for _ in range(10)]

    for bh in range(10):
        for bw in range(10):
            if Ass[bh][bw] == 'o':
                continue

            if solve(Ass, (bh, bw)):
                print("YES")
                return

    print('NO')


if __name__ == '__main__':
    main()
