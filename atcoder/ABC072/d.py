
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    Ps = lmap(int, input().split())
    cnt = 0

    for i in range(n - 1):
        if i + 1 == Ps[i]:
            Ps[i], Ps[i + 1] = Ps[i + 1], Ps[i]
            cnt += 1

    if Ps[-1] == n:
        cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
