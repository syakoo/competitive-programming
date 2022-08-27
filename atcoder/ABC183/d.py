import heapq


def main():
    n, w = map(int, input().split())
    STPs = [list(map(int, input().split())) for _ in range(n)]
    TPs = []
    for stp in STPs:
        heapq.heappush(TPs, (stp[0], stp[2]))
        heapq.heappush(TPs, (stp[1], -stp[2]))

    wa = 0
    while len(TPs) > 0:
        tp = heapq.heappop(TPs)
        wa += tp[1]
        if wa > w:
            print('No')
            return

    print('Yes')


if __name__ == '__main__':
    main()
