# 30 min
import math
from itertools import combinations


def lmap(func, iter):
    return list(map(func, iter))


def idxs2int(idxs: list) -> int:
    result = 0
    for idx in idxs:
        result += 1 << idx

    return result


def dist(_from: int, _to: int, XYZs: list) -> int:
    x1, y1, z1 = XYZs[_from]
    x2, y2, z2 = XYZs[_to]
    return abs(x1 - x2) + abs(y1 - y2) + max(0, z2 - z1)


def main():
    n = int(input())
    XYZs = [lmap(int, input().split()) for _ in range(n)]

    dp = [[math.inf for _ in range(n)] for _ in range(1 << n)]
    dp[1][0] = 0
    for i in range(2, n+1):
        for idxs in combinations(range(n), i):
            biti = idxs2int(idxs)
            for _to in idxs:
                _from_biti = biti ^ (1 << _to)
                for _from in idxs:
                    if _from == _to:
                        continue

                    dp[biti][_to] = min(
                        dp[biti][_to], dp[_from_biti][_from] + dist(_from, _to, XYZs))

    print(min(map(lambda xs: xs[1] + dist(xs[0], 0, XYZs), enumerate(dp[-1]))))


if __name__ == '__main__':
    main()
