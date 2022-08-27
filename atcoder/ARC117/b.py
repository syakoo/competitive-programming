
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    As.sort()
    subs = [1]*(n-1)

    for i in range(n - 1):
        subs[i] += As[i + 1] - As[i]

    ans = As[0] - 0 + 1
    for sub in subs:
        ans *= sub
        ans %= 10**9 + 7

    print(ans)


if __name__ == '__main__':
    main()
