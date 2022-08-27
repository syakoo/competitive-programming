
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ass = [lmap(int, input().split()) for _ in range(2)]
    s = sum(Ass[1]) + Ass[0][0]

    ans = s
    for i in range(1, n):
        s += Ass[0][i] - Ass[1][i - 1]
        ans = max(ans, s)

    print(ans)


if __name__ == '__main__':
    main()
