from heapq import *


def lmap(func, iter):
    return list(map(func, iter))


def main():
    q = int(input())
    Qs = [input() for _ in range(q)]

    mn = 1 << 60
    que = []
    sm = 0
    for Q in Qs:
        if Q[0] == '3':
            x = heappop(que)
            print(x + sm)
            continue

        t, x = map(int, Q.split())
        if t == 1:
            heappush(que, x - sm)
        else:
            sm += x


if __name__ == '__main__':
    main()
