# 21 min
import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(n)]

    ABs.sort()
    ans = 0
    ni = 0
    q = []
    for mi in range(1, m+1):
        while ni < n and ABs[ni][0] <= mi:
            heapq.heappush(q, -ABs[ni][1])
            ni += 1

        if q:
            ans += -heapq.heappop(q)

    print(ans)


if __name__ == '__main__':
    main()
