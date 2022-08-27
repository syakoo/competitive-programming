
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ATs = [lmap(int, input().split()) for _ in range(n)]
    q = int(input())
    xs = lmap(int, input().split())

    adder = 0
    filters = []
    for a, t in ATs:
        if t == 1:
            adder += a
        elif t == 2:
            filters.append(('max', a - adder))
        else:
            filters.append(('min', a - adder))

    filters.reverse()
    for x in xs:
        ans = None
        for fil in filters:
            if fil[0] == 'max' and fil[1] >= x:
                ans = fil[1] + adder
                break

            if fil[0] == 'min' and fil[1] <= x:
                ans = fil[1] + adder
                break

        if ans is None:
            ans = x + adder

        print(ans)


if __name__ == '__main__':
    main()
