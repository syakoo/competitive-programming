def lmap(func, iter):
    return list(map(func, iter))


def main():
    x, y, z, k = map(int, input().split())
    As = lmap(int, input().split())
    Bs = lmap(int, input().split())
    Cs = lmap(int, input().split())

    Cs.sort(reverse=True)
    ABs = []
    for a in As:
        for b in Bs:
            ABs.append(a+b)

    ABs.sort(reverse=True)
    ABs = ABs[:k]

    ABCs = []
    for ab in ABs:
        for c in Cs:
            ABCs.append(ab + c)

    ABCs.sort(reverse=True)
    for i in range(k):
        print(ABCs[i])


if __name__ == '__main__':
    main()
