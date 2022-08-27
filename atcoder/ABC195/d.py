
def lmap(func, iter):
    return list(map(func, iter))


def solve(WVs, Xs):
    XVs = [0] * len(Xs)
    for w, v in WVs:
        for i, x in enumerate(Xs):
            if x >= w and XVs[i] == 0:
                XVs[i] = v
                break

    return sum(XVs)


def main():
    n, m, q = map(int, input().split())
    WVs = [lmap(int, input().split()) for _ in range(n)]
    WVs.sort(key=lambda x: x[1], reverse=True)
    Xs = lmap(int, input().split())
    Qs = [lmap(int, input().split()) for _ in range(q)]

    for l, r in Qs:
        QXs = Xs[:l-1] + Xs[r:]
        QXs.sort()
        print(solve(WVs, QXs))


if __name__ == '__main__':
    main()
