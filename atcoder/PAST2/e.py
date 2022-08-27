
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(lambda x: int(x) - 1, input().split())
    anss = []

    for i in range(n):
        cnt = 1
        x = As[i]
        while x != i:
            cnt += 1
            x = As[x]

        anss.append(cnt)

    print(*anss)


if __name__ == '__main__':
    main()
