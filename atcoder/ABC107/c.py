
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, k = map(int, input().split())
    Xs = lmap(int, input().split())
    ans = 10**9

    for i in range(n - k + 1):
        if Xs[i] < 0 and Xs[i + k - 1] > 0:
            value = Xs[i + k - 1] - Xs[i] + min(abs(Xs[i]), abs(Xs[i + k - 1]))
        else:
            value = max(abs(Xs[i]), abs(Xs[i + k - 1]))

        ans = min(ans, value)

    print(ans)


if __name__ == '__main__':
    main()
