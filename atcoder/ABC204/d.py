import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ts = lmap(lambda x: -int(x), input().split())

    heapq.heapify(Ts)
    ans = 0
    while len(Ts) >= 2:
        a = heapq.heappop(Ts)
        b = heapq.heappop(Ts)
        ans += min(-a, -b)
        if abs(a-b) != 0:
            heapq.heappush(Ts, -abs(a-b))

    if Ts:
        a = heapq.heappop(Ts)
        ans += -a

    print(ans)


if __name__ == '__main__':
    main()
