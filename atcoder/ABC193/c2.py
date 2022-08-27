
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    i = 2
    cnt = 0
    sq = int(math.sqrt(n))
    f = [False] * (sq + 1)

    for i in range(2, int(math.sqrt(n)) + 1):
        if f[i]:
            continue
        cnt += int(math.log(n, i)) - 1

        x = i
        while True:
            x *= i
            if x > sq:
                break

            f[x] = True

    print(n - cnt)


if __name__ == '__main__':
    main()
