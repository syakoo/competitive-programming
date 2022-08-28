# https://algo-method.com/tasks/336
import sys

sys.setrecursionlimit(10**9)


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n, m = lmap(int, input().split())
    As = lmap(int, input().split()) + [0]
    dp = 1

    for ni in range(n):
        dp |= dp << As[ni]
        dp %= 1 << m

    cnt = 0
    while dp > 0:
        cnt += dp & 1
        dp >>= 1

    print(cnt)


if __name__ == '__main__':
    main()
