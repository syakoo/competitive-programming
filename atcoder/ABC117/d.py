import math
import itertools as it


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    As = lmap(int, input().split())

    if k == 0:
        print(sum(As))
        return

    maxbit = int(math.log2(k)) + 1
    cnts = [0]*(maxbit+1)
    for b in range(maxbit):
        for a in As:
            cnts[b] += (a >> b) & 1

    def g(b: int) -> int:
        res = (n - cnts[b]*2) * (1 << b)
        if res < 0:
            return 0
        return res
    Baccums = list(it.accumulate(map(g, range(maxbit))))

    def f(b: int) -> int:
        if b == 0:
            return g(0)*(k % 2)

        if k >> b & 1:
            return max(Baccums[b-1], g(b) + f(b-1))
        else:
            return f(b-1)

    print(sum(As) + f(maxbit - 1))


if __name__ == '__main__':
    main()
