import math
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ass = [set(input()) for _ in range(n)]

    if n == 1:
        print(Ass[0].pop())
        return

    values = []
    for i in range(n//2):
        inters = Ass[i].intersection(Ass[-i-1])
        if not len(inters):
            print(-1)
            return

        values.append(inters.pop())

    if n % 2 == 0:
        ans = ''.join(values + values[::-1])
    else:
        ans = ''.join(values + [str(Ass[n//2].pop())]+ values[::-1])

    print(ans)


if __name__ == '__main__':
    main()
