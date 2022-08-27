
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ass = [lmap(int, input().split()) for _ in range(2)]

    s_A0 = [0] * n
    s_A1 = [0] * n
    s_A0[0] = Ass[0][0]
    s_A1[-1] = Ass[1][-1]
    for i in range(1, n):
        s_A0[i] += s_A0[i - 1] + Ass[0][i]
        s_A1[-i-1] += s_A1[-i] + Ass[1][-i-1]

    ans = 0
    for i in range(n):
        ans = max(ans, s_A0[i] + s_A1[i])

    print(ans)


if __name__ == '__main__':
    main()
