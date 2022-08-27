from itertools import product


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    k = int(input())
    CDs = [lmap(int, input().split()) for _ in range(k)]

    ans = 0
    for cds in product(*CDs):
        dishes = [0] * (n + 1)
        cnt = 0
        for cd in cds:
            dishes[cd] += 1

        for a, b in ABs:
            if dishes[a] and dishes[b]:
                cnt += 1

        ans = max(ans, cnt)

    print(ans)


if __name__ == '__main__':
    main()
