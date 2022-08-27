
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    k = int(input())
    CDs = [lmap(int, input().split()) for _ in range(k)]
    ans = 0

    for i in range(2**k):
        bolls = [0 for _ in range(n + 1)]
        fixed_bin = ("0000000" + str(bin(i))[2:])[-k:]
        for j, bi in enumerate(fixed_bin):
            bolls[CDs[j][int(bi)]] += 1

        count = 0
        for a, b in ABs:
            if bolls[a] >= 1 and bolls[b] >= 1:
                count += 1

        ans = max(ans, count)

    print(ans)


if __name__ == '__main__':
    main()
