
def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    Hs = lmap(int, input().split())
    ABs = [lmap(int, input().split()) for _ in range(m)]
    cnts = [0] * n

    for a, b in ABs:
        # O(M)
        if Hs[a - 1] == Hs[b - 1]:
            cnts[a - 1] += 1
            cnts[b - 1] += 1
        elif Hs[a - 1] > Hs[b - 1]:
            cnts[b - 1] += 1
        else:
            cnts[a - 1] += 1

    print(cnts.count(0))


if __name__ == '__main__':
    main()
