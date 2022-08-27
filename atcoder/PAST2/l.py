import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k, d = map(int, input().split())
    As = lmap(int, input().split())

    if n < d * (k - 1) + 1:
        print(-1)
        return

    que = []
    currd = 0
    ai = 0
    anss = []
    for ki in range(k):
        while ai < n - d*(k - ki - 1):
            heapq.heappush(que, (As[ai], ai))
            ai += 1

        a, i = heapq.heappop(que)
        while i < currd:
            a, i = heapq.heappop(que)

        anss.append(a)
        currd = i + d

    print(*anss)


if __name__ == '__main__':
    main()
