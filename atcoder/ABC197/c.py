
import math


def lmap(func, iter):
    return list(map(func, iter))


def main():
    n = int(input())
    As = lmap(int, input().split())
    ans = 2**30

    if n == 1:
        print(As[0])
        return

    for i in range(1, 1 << n-1):
        x = As[0]
        y = 0
        for j in range(1, n):
            if not (i & (1 << (j - 1))):
                x |= As[j]
            else:
                y ^= x
                x = As[j]

        ans = min(ans, y ^ x)

    print(ans)


if __name__ == '__main__':
    main()
