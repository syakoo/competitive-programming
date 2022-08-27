# 22 min
import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def solve(h: int, w: int) -> int:
    ans = 10**9
    for hi in range(1, h // 2 + 1):
        rh = h - hi
        if rh % 2 == 0 or w % 2 == 0:
            ans = min(ans, abs(hi*w - rh*w // 2))
        else:
            areas = []
            if rh < w:
                areas.append(hi*w)
                areas.append((w//2) * rh)
                areas.append((w//2 + 1) * rh)
            else:
                areas.append(hi*w)
                areas.append((rh//2) * w)
                areas.append((rh//2 + 1) * w)
            ans = min(ans, max(areas) - min(areas))

    return ans


def main():
    h, w = map(int, input().split())
    print(min(solve(h, w), solve(w, h)))


if __name__ == '__main__':
    main()
