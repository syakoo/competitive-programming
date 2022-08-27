
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    XCs = [lmap(int, input().split()) for _ in range(n)]
    XCs.sort(lambda x: x[1])
    Cs = [[0, 0]]
    _c = 0
    for x, c in XCs:
        if _c != c:
            Cs.append([x, x])
            _c = c
        else:
            Cs[-1] = [min(Cs[-1][0], x), max(Cs[-1][1], x)]

    dp = [[0 for _ in range(2)] for _ in range(len(Cs))]

    for i in range(len(Cs) - 1):
        l, r = Cs[i + 1]
        nl = min(dp[i][0] + abs(Cs[i][0]-r) + (r - l),
                 dp[i][1] + abs(Cs[i][1]-r) + (r - l))
        nr = min(dp[i][0] + abs(Cs[i][0]-l) + (r - l),
                 dp[i][1] + abs(Cs[i][1]-l) + (r - l))
        dp[i + 1] = [nl, nr]

    print(min(dp[-1][0] + abs(Cs[-1][0]), dp[-1][1] + abs(Cs[-1][1])))


if __name__ == '__main__':
    main()
