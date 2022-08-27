# 17 min

def lmap(func, iter):
    return list(map(func, iter))


def main():
    h, w, d = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(h)]
    flags = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    q = [(0, 0)]

    for i in range(d, -1, -1):
        n_q = []
        for hi, wi in q:
            if i % 2 == 0:
                ans = max(ans, Ass[hi][wi])

            for dh, dw in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                nh, nw = hi + dh, wi + dw

                if 0 <= nh < h and 0 <= nw < w and not flags[nh][nw]:
                    flags[nh][nw] = True
                    n_q.append((nh, nw))

        q = n_q

    print(ans)


if __name__ == '__main__':
    main()
