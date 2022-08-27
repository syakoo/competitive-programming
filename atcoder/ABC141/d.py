import math
import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    As = lmap(lambda x: -int(x), input().split())

    heapq.heapify(As)

    for _ in range(m):
        it = heapq.heappop(As)
        heapq.heappush(As, math.ceil(it / 2))

    print(-sum(As))


if __name__ == '__main__':
    main()
