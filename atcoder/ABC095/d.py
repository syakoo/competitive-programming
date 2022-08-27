import itertools as it


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, c = map(int, input().split())
    XVs = [[0, 0]] + [lmap(int, input().split()) for _ in range(n)] + [[0, 0]]

    Ls = list(it.accumulate(XVs, func=lambda p0, p1: (p1[0], p1[1]+p0[1])))
    Rs = list(it.accumulate(reversed(XVs), func=lambda p0,
                            p1: (c - p1[0], p1[1]+p0[1])))
    mxLs = list(it.accumulate(Ls, func=lambda p0, p1: max(
        p0, p1, key=lambda xs: xs[1] - xs[0])))
    mxLs2 = list(it.accumulate(Ls, func=lambda p0, p1: max(
        p0, p1, key=lambda xs: xs[1] - 2*xs[0])))

    ans = 0
    for l in range(n, -1, -1):
        r = n - l
        score1 = Rs[l][1] - Rs[l][0] + mxLs[r][1] - mxLs[r][0] - Rs[l][0]
        score2 = Rs[l][1] - Rs[l][0] + mxLs2[r][1] - mxLs2[r][0] - mxLs2[r][0]
        ans = max(ans, score1, score2)

    print(ans)


if __name__ == '__main__':
    main()
