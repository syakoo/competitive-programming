import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ABs = [lmap(int, input().split()) for _ in range(n)]
    ABs.sort(key=lambda x: x[0])
    ABi = 0
    q = []
    ans = 0

    for k in range(1, n + 1):
        while ABi < n and ABs[ABi][0] <= k:
            heapq.heappush(q, -ABs[ABi][1])
            ABi += 1

        ans += -heapq.heappop(q)
        print(ans)


if __name__ == '__main__':
    main()
