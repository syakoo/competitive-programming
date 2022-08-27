
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = map(int, input().split())
    KSs = [lmap(int, input().split()) for _ in range(m)]
    Ps = lmap(int, input().split())
    ans = 0

    for bit in range(1 << n):
        for mi in range(m):
            sm = sum(lmap(lambda s: 1 if bit & 1 <<
                          (s - 1) else 0, KSs[mi][1:]))
            if sm % 2 != Ps[mi]:
                break
        else:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
