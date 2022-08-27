import heapq


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ps = lmap(int, input().split())
    MAX = 2*10**5 + 1
    mps = [0]*MAX
    cur = 0

    for p in ps:
        mps[p] = 1

        while cur < MAX and mps[cur]:
            cur += 1

        print(cur)


if __name__ == '__main__':
    main()
