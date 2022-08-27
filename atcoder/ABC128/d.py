
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Vs = lmap(int, input().split())

    mx = -float("inf")
    for l in range(min(k+1, n)):
        for r in range(n-k+l, n+1):
            if l > r:
                continue
            subVs = Vs[:l] + Vs[r:]
            subVs.sort()
            res = sum(subVs)
            for i in range(min(k - l - (n - r), len(subVs))):
                if subVs[i] >= 0:
                    break
                res -= subVs[i]

            mx = max(mx, res)

    print(mx)


if __name__ == '__main__':
    main()
