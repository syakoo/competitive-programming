import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Ass = [lmap(int, input().split()) for _ in range(n)]

    def jadge(x: int) -> bool:
        cntss = [[0]*n for _ in range(n)]
        for h in range(n):
            for w in range(n):
                if Ass[h][w] > x:
                    for wi in range(max(0, w - k + 1), w + 1):
                        cntss[h][wi] += 1

        for w in range(n-k+1):
            cnt = 0
            for h in range(k):
                cnt += cntss[h][w]

            if cnt >= k**2 // 2:
                return True

            for h in range(k, n):
                hl = h - k
                cnt -= cntss[hl][w]
                cnt += cntss[h][w]

                if cnt >= k**2 // 2:
                    return True

        return False

    l, r = 0, 10**9
    while (r - l) > 1:
        m = (r + l) // 2
        if jadge(m):
            l = m
        else:
            r = m

    print(l)


if __name__ == '__main__':
    main()
