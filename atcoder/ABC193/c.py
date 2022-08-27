
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    ms = [False] * (n+1)
    cnt = 1
    sq = int(math.sqrt(n))

    for i in range(2, sq + 1):
        if ms[i] == True:
            continue
        cnt += 1
        x = i
        while x * i <= n:
            x *= i
            ms[x] = True

    for i in range(sq + 1, n+1):
        if ms[i] == False:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    main()
